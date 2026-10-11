import unittest
import json
import sqlite3
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from Tools.Site import generate_site as site
from Tools.Site.generate_site import extract_script_constants


class ScriptExplorerIndexTests(unittest.TestCase):
    def test_database_categories_are_not_lua_effect_categories(self) -> None:
        # Pot of Greed's DB category is 0x100; Lua CATEGORY_DRAW is 0x10000.
        self.assertEqual(site.category_labels_from_mask(0x100), ['Draw'])
        # Mystic Dealer carries Draw and Type-Related database search flags.
        self.assertEqual(site.category_labels_from_mask(1048832), ['Draw', 'Type-Related'])
        self.assertEqual(site.category_labels_from_mask(-2147483648), ['Negate Effect'])
        self.assertEqual(site.category_labels_from_mask(0x800000000), ['Hand Trap'])

    def test_extracts_named_constants_without_comment_only_matches(self) -> None:
        script = """
        e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
        e1:SetCode(EVENT_ADJUST)
        e1:SetRange(LOCATION_MZONE)
        e1:SetCode(EVENT_ADJUST)
        -- e2:SetCode(EVENT_FREE_CHAIN)
        """

        self.assertEqual(
            extract_script_constants(script),
            [
                "EFFECT_TYPE_CONTINUOUS",
                "EFFECT_TYPE_FIELD",
                "EVENT_ADJUST",
                "LOCATION_MZONE",
            ],
        )

    def test_rush_alias_calls_link_to_canonical_reference(self) -> None:
        names = {"RushDuel.AddEffect", "Duel.Draw"}
        script = "RD.AddEffect(c)\nDuel.Draw(tp,1,REASON_EFFECT)"
        self.assertEqual(site.extract_api_calls(script, names, {}), ["Duel.Draw", "RushDuel.AddEffect"])
        self.assertEqual(site.count_api_calls(script, "RushDuel.AddEffect"), 1)
        self.assertIn("RD.AddEffect", site.extract_call_snippet(script, "RushDuel.AddEffect"))

    def test_standard_and_rush_keep_same_passcode_separate(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            generated = root / "Generated"
            (generated / "rush").mkdir(parents=True)
            for relative, names in (("api_functions.generated.json", ["Duel.Draw"]), ("rush/api_functions.generated.json", ["RushDuel.AddEffect"])):
                (generated / relative).write_text(json.dumps({"functions": [{"name": name} for name in names]}), encoding="utf-8")
            for folder, filename, name in (("Scripts", "cards.cdb", "Standard card"), ("Rush/Scripts", "rush_cards.cdb", "Rush card")):
                scripts = root / folder
                scripts.mkdir(parents=True)
                (scripts / "c123.lua").write_text("RD.AddEffect(c)\nDuel.Draw(tp,1,REASON_EFFECT)", encoding="utf-8")
                with sqlite3.connect(root / filename) as database:
                    database.execute('CREATE TABLE datas (id INTEGER, type INTEGER, atk INTEGER, def INTEGER, level INTEGER, race INTEGER, attribute INTEGER, category INTEGER)')
                    database.execute('CREATE TABLE texts (id INTEGER, name TEXT, desc TEXT)')
                    database.execute('INSERT INTO datas VALUES (123,32777,3000,2500,10,2147483648,1,0)')
                    database.execute('INSERT INTO texts VALUES (123,?,?)', (name, 'Example text'))
                database.close()
            with patch.multiple(site, WORKSPACE=root, GENERATED_DIR=generated,
                                SCRIPTS_DIR=root / 'Scripts', RUSH_SCRIPTS_DIR=root / 'Rush/Scripts',
                                CARDS_DB=root / 'cards.cdb', RUSH_CARDS_DB=root / 'rush_cards.cdb'):
                standard = site.scan_examples()[0][0]
                rush = site.scan_examples('rush')[0][0]
            self.assertEqual(standard['name'], 'Standard card')
            self.assertEqual(rush['name'], 'Rush card')
            self.assertNotIn('Legend', standard['card_type_labels'])
            self.assertIn('Legend', rush['card_type_labels'])
            self.assertIn('Maximum', rush['card_type_labels'])
            self.assertNotIn('RushDuel.AddEffect', standard['api_calls'])
            self.assertEqual(rush['api_links']['RushDuel.AddEffect'], '/rush/api/functions/RushDuel/AddEffect')
            self.assertEqual(rush['api_links']['Duel.Draw'], '/api/functions/Duel/Draw')
            self.assertNotEqual(site.example_link(standard), site.example_link(rush))
            self.assertEqual(rush['race'], 2147483648)

    def test_missing_database_fails_instead_of_silently_losing_card_text(self) -> None:
        with TemporaryDirectory() as directory:
            with self.assertRaises(FileNotFoundError):
                site.load_cards(Path(directory) / 'missing.cdb')

    def test_generation_preserves_authored_navigation(self) -> None:
        with TemporaryDirectory() as directory:
            docs = Path(directory)
            (docs / '.vitepress').mkdir()
            config = docs / '.vitepress/config.mts'
            config.write_text('// authored lessons and navigation', encoding='utf-8')
            with patch.object(site, 'DOCS_DIR', docs):
                site.write_navigation([])
            self.assertEqual(config.read_text(encoding='utf-8'), '// authored lessons and navigation')
            self.assertTrue((docs / '.vitepress/navigation.generated.json').exists())


if __name__ == "__main__":
    unittest.main()
