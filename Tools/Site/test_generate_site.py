import unittest

from Tools.Site.generate_site import extract_script_constants


class ScriptExplorerIndexTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
