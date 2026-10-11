import json
import tempfile
import unittest
from pathlib import Path

from Tools.FunctionDocs import generate_function_docs as api
from Tools.FunctionDocs.rush_function_docs import generate_rush_docs, prose


class RushReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workspace = Path(__file__).resolve().parents[2]
        cls.temporary = tempfile.TemporaryDirectory()
        cls.output = Path(cls.temporary.name)
        cls.count, cls.constant_count = generate_rush_docs(cls.workspace, cls.output, api)
        cls.payload = json.loads((cls.output / "api_functions.generated.json").read_text(encoding="utf-8"))
        cls.docs = {doc["name"]: doc for doc in cls.payload["functions"]}

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def test_multiline_signatures_keep_all_parameters(self):
        doc = self.docs["RushDuel.CostSendMatchToGrave"]
        self.assertEqual([param["name"] for param in doc["params"]], [
            "filter", "field", "min", "max", "except_self", "hint_selection",
            "confirm", "set_label_before", "set_object_before", "set_label_after", "set_object_after",
        ])
        self.assertEqual(doc["returns"][0]["type"], "any")

    def test_bootstrap_order_selects_the_runtime_definition(self):
        doc = self.docs["RushDuel.ConfirmCardFilter"]
        self.assertTrue(doc["source_files"][0]["path"].endswith("RDRitual.lua"))
        shadowed = self.payload["metadata"]["shadowed_declarations"]
        self.assertEqual(len(shadowed), 1)
        self.assertTrue(shadowed[0]["replaced"]["path"].endswith("RDFusion.lua"))

    def test_public_names_and_aliases_stay_separate_from_native_api(self):
        self.assertEqual(len(self.docs), self.count)
        for doc in self.docs.values():
            self.assertEqual(doc["namespace"], "RushDuel")
            self.assertFalse(doc["short_name"].startswith("_"))
            self.assertFalse(doc["core_binding"])
            self.assertEqual(doc["aliases"], ["RD." + doc["short_name"]])
            page = self.output / "wiki" / "api" / "functions" / "RushDuel" / (doc["short_name"] + ".md")
            self.assertTrue(page.is_file(), doc["name"])

    def test_editor_exports_include_both_aliases_and_only_constants(self):
        records = api.parse_bullet_file(self.output / "_function_english.generated.txt")
        self.assertIn("RD.AddMaximumProcedure", records)
        self.assertIn("RushDuel.AddMaximumProcedure", records)
        constants = api.parse_constant_docs(self.output / "constant_english.generated.lua", self.output, "test")
        self.assertEqual(len(constants), self.constant_count)
        self.assertEqual(constants["TYPE_LEGEND"].value, "0x8")
        self.assertEqual(constants["TYPE_MAXIMUM"].value, "0x8000")
        for line in (self.output / "constant_english.generated.lua").read_text(encoding="utf-8").splitlines():
            self.assertTrue(line.startswith("--") or " = " in line)

    def test_reviewed_return_contracts_do_not_claim_void_for_factories(self):
        self.assertEqual(self.docs["RushDuel.CostPayLP"]["returns"][0]["type"], "function")
        self.assertEqual(self.docs["RushDuel.Select"]["returns"][0]["type"], "Group|nil")
        self.assertEqual(self.docs["RushDuel.AddMaximumProcedure"]["returns"], [])

    def test_prose_escapes_html_without_damaging_inline_code(self):
        self.assertEqual(prose("Loads c<code>.lua; use `count < 2`."),
                         "Loads c&lt;code&gt;.lua; use `count < 2`.")
        page = (self.output / "wiki/api/functions/RushDuel/AlternateCard.md").read_text(encoding="utf-8")
        self.assertIn("c&lt;code&gt;.lua", page)
        self.assertNotIn("c<code>.lua", page)
        unreviewed = (self.output / "wiki/api/functions/RushDuel/ConfirmCardFilter.md").read_text(encoding="utf-8")
        self.assertIn("### Upstream source comment\n\n```text", unreviewed)


class NativeCacheTests(unittest.TestCase):
    def test_missing_external_core_retains_cached_bindings_without_stub(self):
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            out = workspace / "Generated" / "FunctionDocs" / "api_functions.generated.json"
            doc = api.FunctionDoc(
                name="Card.GetCardType", namespace="Card", short_name="GetCardType",
                params=[], returns=[], core_binding=True,
                source_files=[api.SourceRef("missing/libcard.cpp", 1, "core")],
            )
            api.write_json(out, [doc], {})
            docs = api.load_all_function_docs(workspace, workspace / "absent-core")
            self.assertIn("Card.GetCardType", docs)
            self.assertTrue(docs["Card.GetCardType"].core_binding)
            self.assertEqual(docs["Card.GetCardType"].returns[0].type, "int")


if __name__ == "__main__":
    unittest.main()
