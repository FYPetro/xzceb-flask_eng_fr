import unittest
import translator

class TestMachineTranslation(unittest.TestCase):
    def test_french_to_english_null(self):
        frenchText = ""
        englishText = translator.french_to_english(frenchText)
        self.assertEqual(englishText,"")

    def test_english_to_french_null(self):
        englishText = ""
        frenchText = translator.english_to_french(englishText)
        self.assertEqual(frenchText,"")

    def test_french_to_english_bonjour(self):
        frenchText = "Bonjour"
        englishText = translator.french_to_english(frenchText)
        self.assertEqual(englishText,"Hello")

    def test_english_to_french_hello(self):
        englishText = "Hello"
        frenchText = translator.english_to_french(englishText)
        self.assertEqual(frenchText,"Bonjour")

if __name__ == '__main__':
    unittest.main()
