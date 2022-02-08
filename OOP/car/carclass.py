class CarClass:
    def __init__(self, brand, model, year, probeg):
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = probeg

    def show_car(self):
        print(f'{self.brand}, {self.model}, Год выпуска: {self.year}, Пробег: {self.probeg} км')


if __name__ == "__main__":
    e = CarClass('Tesla', 'S', 2022, 5000)
    e.show_car()

