import unittest
from random import choice, randint

from app import Figure  # файл app.py повинен бути в одній директорії з тестами

class TestFigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Виконається лише раз на початку тестів."""
        pass
    
    def setUp(self) -> None:
        """Виконується кожного разу, коли запускається тест."""
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(f"Тестуємо вивід: має бути '{self.figure}' == '{self.obj.get_figure_type}'")
        self.assertEqual(
            self.figure, 
            self.obj.get_figure_type, 
            "Властивість get_figure_type повертає неправильну фігуру!"
        )

    def test_figure_lengh(self):
        # Цей тест буде провалено, бо повертається self.type, а не self.length
        self.assertEqual(
            self.length, 
            self.obj.get_figure_length, 
            "Властивість get_figure_length повертає неправильну довжину!"
        )
    
    def test_obj(self):
        # Перевірка створення об'єкта з недозволеними параметрами – має бути AssertionError
        with self.assertRaises(AssertionError):
            Figure("коло", 1)
    
    def test_description(self):
        # Юніт тест для нової функціональності – методу description
        expected = f"Фігура: {self.figure}, довжина: {self.length}"
        self.assertEqual(
            expected, 
            self.obj.description(), 
            "Метод description повертає неправильний опис!"
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)
