import unittest
from app.utilities.id_converter import convert_id, convert_id_from_url


class TestIdConversion(unittest.TestCase):
    def test_conversion(self):
        ## Formatted steamID3 means removing the following characters from ID
        ## "[U:1:"  "]"
        # Test id conversion from steamID to formatted steamID3
        self.assertEqual(convert_id("STEAM_0:1:35807358"), "71614717")
        # Test id conversion from steamID64 to formatted steamID3
        self.assertEqual(convert_id("76561198031880445"), "71614717")
        # Test id conversion from Steam Profile url to steamID3
        self.assertEqual(convert_id_from_url("https://steamcommunity.com/id/hfacada/"), "71614717")

    def test_values(self):
        # Test raise Value error on wrong or invalid steam url
        self.assertRaises(ValueError, convert_id, "STEAM_0:1:not_even_anID")
        self.assertRaises(ValueError, convert_id_from_url, "https://awrongurl")
