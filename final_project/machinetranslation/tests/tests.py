import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(""), "") # Test for null input for french_to_english.
        self.assertEqual(english_to_french("Hello"), "Bonjour") # Test for the translation of the world 'Hello' and 'Bonjour'.
        self.assertNotEqual(english_to_french("Hello"), "Oi") # Test that 'Hello' does not translate to 'Oi'.

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(""), "") # Test for null input for english_to_french.
        self.assertEqual(french_to_english("Bonjour"), "Hello") # Test for the translation of the world 'Bonjour' and 'Hello'.
        self.assertNotEqual(french_to_english("Oi"), "Hello") # Test that 'Oi' does not translate to 'Hello'.

unittest.main()
