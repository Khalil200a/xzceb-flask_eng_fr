import unittest

from mmachinetranslation.translator import englishToFrench, frenchToEnglish

class testTranslator(unittest.TestCase):
    def test_englishtoFrench(self):
        self.assertEqual(englishToFrench(" "), " ")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_frenchtoEnglish(self):
        self.assertEqual(frenchToEnglish(" "), " ")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

if __name__=='__main__':
    unittest.main()