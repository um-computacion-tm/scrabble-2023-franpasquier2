import unittest
from game.dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    def test_add_word(self):
        dictionary = Dictionary()
        dictionary.add_word("gato")
        self.assertTrue(dictionary.check_word("gato"))

    def test_check_word(self):
        dictionary = Dictionary()
        dictionary.add_word("gato")
        self.assertTrue(dictionary.check_word("gato"))
        self.assertFalse(dictionary.check_word("pájaro"))

    def test_check_word_case_insensitive(self):
        dictionary = Dictionary()
        dictionary.add_word("gato")
        self.assertTrue(dictionary.check_word("GATO"))
        self.assertTrue(dictionary.check_word("GaTo"))

if __name__ == '__main__':
    unittest.main()
