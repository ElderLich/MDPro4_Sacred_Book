"""Regression coverage for the Card Explorer's source decoding and output."""
from __future__ import annotations

import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from Tools.Site import generate_card_catalog as catalog


def sample_row(**changes):
    row = dict(id=1, name='Sample', desc='', type=0x21, ot=3, alias=0,
               setcode=0, atk=1000, def_=500, level=4, race=1,
               attribute=0x10, category=0)
    row['def'] = row.pop('def_')
    row.update({f'str{i}': '' for i in range(1, 17)})
    row.update(changes)
    return row


class CardDecodingTests(unittest.TestCase):
    def detail(self, row, format_id='standard'):
        return catalog.card_detail(row, format_id, 'sample.cdb', {},
                                   catalog.WORKSPACE, catalog.WORKSPACE / 'Scripts')

    def test_signed_packed_setcodes_preserve_all_four_slots(self):
        packed = 0xabcd012312340001
        signed = packed - (1 << 64)
        result = catalog.decode_setcodes(signed, {1: 'Known'})
        self.assertEqual([item['code'] for item in result], ['0x1', '0x1234', '0x123', '0xabcd'])
        self.assertEqual(result[0]['name'], 'Known')
        self.assertIsNone(result[-1]['name'])
        self.assertEqual(self.detail(sample_row(setcode=signed))['raw']['setcode'], hex(packed))

    def test_unknown_archetype_is_explicit_not_invented(self):
        detail = self.detail(sample_row(setcode=0xbeef))
        self.assertEqual(detail['archetypes'], ['Unknown (0xbeef)'])
        self.assertEqual(catalog.decode_setcodes(0, {}), [])

    def test_signed_rush_cyborg_and_unknown_race_bits(self):
        detail = self.detail(sample_row(race=-2147483648), 'rush')
        self.assertEqual(detail['race'], 'Cyborg')
        self.assertEqual(detail['raw']['race'], '0x80000000')
        self.assertEqual(catalog.decode_mask(0x80, catalog.ATTRIBUTE_LABELS), ['Unknown (0x80)'])

    def test_scale_byte_order_and_monster_level(self):
        detail = self.detail(sample_row(type=0x1000021, level=(3 << 24) | (9 << 16) | 7))
        self.assertEqual(detail['scales'], {'left': 3, 'right': 9})
        self.assertEqual(detail['level'], 7)

    def test_link_defense_is_arrows_and_xyz_is_rank(self):
        detail = self.detail(sample_row(type=0x4000021, level=3, **{'def': 0x80 | 0x1 | 0x4}))
        self.assertIsNone(detail['defense'])
        self.assertEqual(detail['linkMarkers'], ['Top', 'Bottom-left', 'Bottom-right'])
        self.assertEqual(detail['levelLabel'], 'Link')
        self.assertEqual(self.detail(sample_row(type=0x800021))['levelLabel'], 'Rank')

    def test_nonmonster_stats_are_absent_and_unknown_atk_stays_unknown(self):
        detail = self.detail(sample_row(type=2))
        self.assertIsNone(detail['attack'])
        self.assertIsNone(detail['defense'])
        self.assertIsNone(detail['level'])
        self.assertEqual(self.detail(sample_row(atk=-2))['attack'], -2)

    def test_pendulum_text_and_original_are_preserved(self):
        source = 'Pendulum Scale = 3\r\n[ Pendulum Effect ]\r\nPendulum body.\r\n----------\r\n[ Monster Effect ]\r\nMonster body.'
        result = catalog.split_description(source, 0x1000021, 'standard')
        self.assertEqual(result['pendulumText'], 'Pendulum body.')
        self.assertEqual(result['effectText'], 'Monster body.')
        self.assertEqual(result['originalText'], source)

    def test_pendulum_without_effect_and_unfamiliar_layout_are_lossless(self):
        source = 'Pendulum Scale = 5\n--------\n[ Monster Effect ]\nMajespecter body.'
        result = catalog.split_description(source, 0x1000021, 'standard')
        self.assertEqual(result['pendulumText'], '')
        self.assertEqual(result['effectText'], 'Majespecter body.')
        result = catalog.split_description('Unfamiliar format\nKeep all text', 0x1000021, 'standard')
        self.assertEqual(result['effectText'], 'Unfamiliar format\nKeep all text')
        unknown_prefix = 'Do not discard this text.\n[ Monster Effect ]\nMonster body.'
        self.assertEqual(catalog.split_description(unknown_prefix, 0x1000021, 'standard')['effectText'], unknown_prefix)
        reversed_headers = '[ Monster Effect ]\nMonster body.\n[ Pendulum Effect ]\nPendulum body.'
        self.assertEqual(catalog.split_description(reversed_headers, 0x1000021, 'standard')['effectText'], reversed_headers)

    def test_rush_maximum_preamble_requirement_and_continuous_effect(self):
        source = 'RD/KP01-JP001\nMaximum ATK: 3,500\t\nSummon using L and R.\n[REQUIREMENT]\t\nMaximum Mode\n[CONTINUOUS EFFECT]\nCannot be destroyed.'
        result = catalog.split_description(source, 0x8021, 'rush')
        self.assertEqual(result['packCode'], 'RD/KP01-JP001')
        self.assertEqual(result['maximumAttack'], 3500)
        self.assertEqual(result['preambleText'], 'Summon using L and R.')
        self.assertEqual(result['requirementText'], 'Maximum Mode')
        self.assertEqual(result['effectHeading'], 'Continuous effect')
        self.assertEqual(result['effectText'], 'Cannot be destroyed.')
        self.assertEqual(result['originalText'], source)

    def test_rush_multi_choice_repeated_sections_and_flavor_text(self):
        source = '[REQUIREMENT]\nNone\n[MULTI-CHOICE EFFECT]\nChoose one:\nFirst.\n[EFFECT]\nSecond.'
        result = catalog.split_description(source, 0x21, 'rush')
        self.assertEqual(result['requirementText'], 'None')
        self.assertIn('Choose one:', result['effectText'])
        self.assertIn('Second.', result['effectText'])
        self.assertEqual(catalog.split_description('A normal monster.', 0x11, 'rush')['effectText'], 'A normal monster.')

    def test_rush_only_type_bits_and_aux_string_indices(self):
        row = sample_row(type=0x8029, str2='Second selectable effect')
        detail = self.detail(row, 'rush')
        self.assertTrue(detail['legend'])
        self.assertIn('Maximum', detail['types'])
        self.assertNotIn('Legend', self.detail(row)['types'])
        self.assertEqual(detail['strings'], [{'index': 1, 'text': 'Second selectable effect'}])

    def test_alias_resolves_only_an_existing_script_and_prefers_direct(self):
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            scripts = workspace / 'Scripts'
            scripts.mkdir()
            (scripts / 'c42.lua').write_text('-- alias', encoding='utf-8')
            self.assertEqual(catalog.script_path(43, 42, scripts, workspace), 'Scripts/c42.lua')
            (scripts / 'c43.lua').write_text('-- own', encoding='utf-8')
            self.assertEqual(catalog.script_path(43, 42, scripts, workspace), 'Scripts/c43.lua')
            self.assertIsNone(catalog.script_path(44, 0, scripts, workspace))

    def test_search_normalizes_fullwidth_and_whitespace(self):
        self.assertEqual(catalog.normalize_search('  Blue\t\uff25yes\nDragon '), 'blue eyes dragon')

    def test_localized_pendulum_headers_keep_separate_text(self):
        variants = [
            ('Pendelbereich = 3\n[ Pendeleffekt ]', '[ Monstereffekt ]'),
            ('←◊3 Escala 3◊→\n【Efecto de Péndulo】', '【Efecto de Monstruo】'),
            ('Échelle Pendule = 3\n[ Effet Pendule ]', '[ Effet de Monstre ]'),
            ('Valore Pendulum = 3\n[ Effetto Pendulum ]', '[ Effetto di un Mostro ]'),
            ('【Ｐスケール：青３／赤３】', '【モンスター効果】'),
            ('【펜듈럼 효과】', '【몬스터 효과】'),
            ('Escala de Pêndulo = 3\n[ Efeito de Pêndulo ]', '[ Efeito de Monstro ]'),
            ('←3 【灵摆】 3→', '【怪兽描述】'),
            ('【靈擺效果】', '【怪獸敘述】'),
        ]
        for pendulum, monster in variants:
            with self.subTest(pendulum=pendulum):
                source = f'{pendulum}\nPendulum body.\n━━━━━━━━━━━━━━━━━━━━━━━\n{monster}\nMonster body.'
                result = catalog.split_description(source, 0x1000021, 'standard')
                self.assertEqual(result['pendulumText'], 'Pendulum body.')
                self.assertEqual(result['effectText'], 'Monster body.')
                self.assertEqual(result['originalText'], source)
        warned = catalog.split_description('（注：暂时无法正常使用）\n←8 【灵摆】 8→\nPendulum body.\n【怪兽效果】\nMonster body.', 0x1000021, 'standard')
        self.assertEqual(warned['preambleText'], '（注：暂时无法正常使用）')
        self.assertEqual(warned['pendulumText'], 'Pendulum body.')
        self.assertEqual(warned['effectText'], 'Monster body.')

    def test_localized_rush_headers_including_mixed_source_languages(self):
        variants = [
            ('[BEDINGUNG]', '[DAUEREFFEKT]'), ('[REQUISITO]', '[EFECTO CONTINUO]'),
            ('[CONDITION]', '[EFFET CONTINU]'), ('[REQUISITO]', '[EFFETTO CONTINUO]'),
            ('【条件】', '【永続効果】'), ('【조건】', '【지속 효과】'),
            ('[REQUISITO]', '[EFEITO CONTÍNUO]'), ('【条件】', '【永续效果】'),
            ('【條件】', '【永續效果】'),
        ]
        for requirement, effect in variants:
            with self.subTest(requirement=requirement, effect=effect):
                source = f'Maximum ATK 3500\n{requirement}\nMaximum Mode\n{effect}\nKeep this effect.'
                result = catalog.split_description(source, 0x8021, 'rush')
                self.assertEqual(result['maximumAttack'], 3500)
                self.assertEqual(result['requirementText'], 'Maximum Mode')
                self.assertEqual(result['effectText'], 'Keep this effect.')
                self.assertEqual(result['effectHeading'], 'Continuous effect')


class CompleteCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.output = Path(cls.temp.name)
        cls.manifest = catalog.write_card_catalogs(output=cls.output)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def index(self, format_id):
        return json.loads((self.output / 'en-US' / format_id / 'index.json').read_text(encoding='utf-8'))

    def detail(self, format_id, card_id):
        record = next(record for record in self.index(format_id)['cards'] if record['id'] == card_id)
        return json.loads((self.output / record['detail']).read_text(encoding='utf-8'))[str(card_id)]

    def test_every_database_card_has_one_index_entry_and_detail(self):
        for format_id, _, filename, _ in catalog.FORMATS:
            rows = catalog.read_cards(catalog.WORKSPACE / filename)
            expected = {int(row['id']) for row in rows}
            records = self.index(format_id)['cards']
            self.assertEqual(len(records), len(expected))
            self.assertEqual({record['id'] for record in records}, expected)
            all_details = {}
            for path in (self.output / 'en-US' / format_id / 'details').glob('*.json'):
                shard = json.loads(path.read_text(encoding='utf-8'))
                self.assertLessEqual(len(shard), catalog.SHARD_SIZE)
                self.assertFalse(set(all_details).intersection(shard))
                all_details.update(shard)
            self.assertEqual(set(all_details), {str(card_id) for card_id in expected})
            for row in rows:
                self.assertEqual(all_details[str(row['id'])]['originalText'], row['desc'] or '')

    def test_descriptions_are_separate_from_initial_index(self):
        index = self.index('standard')
        self.assertNotIn('originalText', index['cards'][0])
        record = next(record for record in index['cards'] if record['id'] == 89631139)
        self.assertNotIn('virtually invincible', record['searchText'])
        search_text = json.loads((self.output / 'en-US/standard/search-text.json').read_text(encoding='utf-8'))
        self.assertIn('virtually invincible', search_text['89631139'])

    def test_known_cards_cover_no_script_alias_pendulum_link_and_rush(self):
        no_script = self.detail('standard', 32864)
        self.assertEqual(no_script['name'], 'The 13th Grave')
        self.assertIsNone(no_script['scriptPath'])
        pendulum = self.detail('standard', 16178681)
        self.assertTrue(pendulum['pendulumText'])
        self.assertNotIn('Pendulum Scale', pendulum['effectText'])
        self.assertEqual(pendulum['scales'], {'left': 4, 'right': 4})
        self.assertIn('Odd-Eyes', pendulum['archetypes'])
        no_pendulum_effect = self.detail('standard', 645794)
        self.assertEqual(no_pendulum_effect['pendulumText'], '')
        self.assertNotIn('Pendulum Scale', no_pendulum_effect['effectText'])
        self.assertTrue(no_pendulum_effect['effectText'].startswith('When this card'))
        link = self.detail('standard', 1861629)
        self.assertEqual(link['name'], 'Decode Talker')
        self.assertEqual(link['linkMarkers'], ['Top', 'Bottom-left', 'Bottom-right'])
        self.assertIsNone(link['defense'])
        maximum = self.detail('rush', 120150002)
        self.assertEqual(maximum['maximumAttack'], 3500)
        self.assertEqual(maximum['requirementText'], 'Maximum Mode')
        self.assertIn('Maximum Summon', maximum['preambleText'])
        self.assertEqual(maximum['effectHeading'], 'Continuous effect')
        self.assertEqual(self.detail('rush', 120196001)['race'], 'Cyborg')

    def test_manifest_has_pinned_sources_and_no_sqlite_sidecars(self):
        self.assertEqual({item['id'] for item in self.manifest['locales'][0]['formats']}, {'standard', 'rush'})
        for source in self.manifest['locales'][0]['formats']:
            self.assertEqual(len(source['sourceSha256']), 64)
            self.assertEqual(source['count'], len(self.index(source['id'])['cards']))
        self.assertEqual(len(self.manifest['locales'][0]['archetypeSource']['sha256']), 64)


class OfflineLocaleTests(unittest.TestCase):
    def test_default_generation_preserves_localized_snapshots_without_source_repo(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            detail_path = 'de-DE/standard/details/0000.json'
            original_bytes = b'{"1":{"name":"Lokalisierte Karte"}}\n'
            (output / detail_path).parent.mkdir(parents=True)
            (output / detail_path).write_bytes(original_bytes)
            catalog.write_json(output / 'de-DE/standard/index.json', {'cards': [{'id': 1, 'detail': detail_path}]})
            catalog.write_json(output / 'de-DE/standard/search-text.json', {'1': 'text'})
            locale = {'id': 'de-DE', 'label': 'German', 'nativeLabel': 'Deutsch', 'formats': [{
                'id': 'standard', 'count': 1, 'index': 'de-DE/standard/index.json',
                'searchText': 'de-DE/standard/search-text.json'}]}
            catalog.write_json(output / 'manifest.json', {'schemaVersion': 2, 'locales': [locale]})
            manifest = catalog.write_card_catalogs(output=output)
            self.assertEqual([item['id'] for item in manifest['locales']], ['en-US', 'de-DE'])
            self.assertEqual((output / detail_path).read_bytes(), original_bytes)
            self.assertEqual(manifest['locales'][1], locale)
            (output / detail_path).unlink()
            with self.assertRaises(FileNotFoundError):
                catalog.write_card_catalogs(output=output)

    def test_committed_locale_snapshots_keep_each_sources_actual_count(self):
        output = catalog.WORKSPACE / 'docs/public/data/cards'
        manifest = json.loads((output / 'manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(manifest['defaultLocale'], 'en-US')
        self.assertEqual({locale['id'] for locale in manifest['locales']}, set(catalog.LOCALES))
        for locale in manifest['locales']:
            catalog.validate_locale_snapshot(output, locale)
            counts = {source['id']: source['count'] for source in locale['formats']}
            expected_standard = {'zh-CN': 15018, 'zh-TW': 14779}.get(locale['id'], 15019)
            self.assertEqual(counts, {'standard': expected_standard, 'rush': 4076})


if __name__ == '__main__':
    unittest.main()
