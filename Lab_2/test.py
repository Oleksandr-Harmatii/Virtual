import unittest
from random import choice, randint

from app import Figure # назва файлу з нашим класом повинна бути app.py

class TestFigure(unittest.TestCase):
    @property
    def get_angles(self):
        if self.type in ["квадрат", "прямокутник"]:
           return 4
        if self.type == "трикутник":
            return 3
    def test_get_angles():
        """Тестуємо чи правильно повертається кількість кутів фігури.
        """
        fig = "трикутник"
        triangle = Figure(fig, 1)
        assert triangle.get_angles == 3, f"У {fig} є 3 кути!"
    @classmethod
    
    def test_app_triangle():
        """Test if we create triangle figure."""
        fig = "трикутник"
        triangle = Figure(fig, 4)
        assert triangle.type == fig, f"Фігура має бути {fig}"
    def setUpClass(cls):
        """Виконається лише раз на початку тестів
        """
        pass
    
    def setUp(self) -> None:
        """Виконується кожного разу коли запускається тест
        """
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(f"Тестуємо вивід, має бути: {self.figure} == {self.obj.get_figure_type}")
        self.assertEqual(self.figure, self.obj.get_figure_type, "Властивість get_figure_type повертає непривильну фігуру!")

    def test_figure_lengh(self):
        self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає непривильну довжину!")
    
    def test_obj(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1) # Спробуємо створити обєкт з недозволеними параметрими, в нас має бути помилка AssertionError


if __name__ == '__main__':
    unittest.main() # unittest.main(verbosity=2) щоб був більш детальний вивід
    