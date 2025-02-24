class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.type  # Помилка: має повертатися self.length


figure1 = Figure("квадрат", 5)
figure2 = Figure("прямокутник", 10)

print(figure1.get_figure_type)  # Виведе: квадрат
print(figure1.get_figure_length)  # ПОМИЛКА: Виведе "квадрат", а має бути 5

print(figure2.get_figure_type)  # Виведе: прямокутник
print(figure2.get_figure_length)  # ПОМИЛКА: Виведе "прямокутник", а має бути 10
