# test.py
import unittest
from main import reverse_string

class TestReverseString(unittest.TestCase):
    def test_basic(self):
        """Перевіряємо базовий випадок перевертання рядка."""
        self.assertEqual(reverse_string("abc"), "cba")
    def test_spaces(self):
        """Перевірка рядка з пробілами."""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
    
    def test_special_characters(self):
        """Перевірка рядка з спеціальними символами."""
        self.assertEqual(reverse_string("a!b@c#"), "#c@b!a")

if __name__ == "__main__":
    unittest.main()
