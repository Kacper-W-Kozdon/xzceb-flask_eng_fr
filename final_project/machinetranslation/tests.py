import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(" ")['translations'][0]['translation'], " ")
        self.assertEqual(french_to_english("Bonjour")['translations'][0]['translation'].lower(), "Hello".lower())

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(" ")['translations'][0]['translation'], " ")
        self.assertEqual(english_to_french("Hello")['translations'][0]['translation'].lower(), "Bonjour".lower())

unittest.main()