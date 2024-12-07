import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        # Проверка на корректность цвета
        if self.__is_valid_color(*color):
            self.__color = list(color)
        else:
            self.__color = [0, 0, 0]  # Цвет по умолчанию

        # Проверка на корректность сторон
        if self.__is_valid_sides(*sides):
            if len(sides) == self.sides_count:
                self.__sides = list(sides)
            elif len(sides) < self.sides_count and all(side == sides[0] for side in sides):
                self.__sides = [sides[0]] * self.sides_count
            else:
                self.__sides = [1] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count

        self.filled = False  # По умолчанию фигура не закрашена

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        # Проверка на корректность значений RGB
        if (isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and
                0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return True
        return False

    def set_color(self, r, g, b):
        # Установка нового цвета, если он корректен
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    @staticmethod
    def __is_valid_sides(*sides):
        # Проверка на корректность сторон
        if all(isinstance(side, int) and side > 0 for side in sides):
            return True
        return False

    def set_sides(self, *new_sides):
        # Установка новых сторон, если они корректны и их количество совпадает с sides_count
        if self.__is_valid_sides(*new_sides):
            if len(new_sides) == self.sides_count:
                self.__sides = list(new_sides)

    def __len__(self):
        # Возвращает периметр фигуры
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        # Возвращает площадь круга
        if len(self.get_sides()) >= 1:
            circumference = self.get_sides()[0]
            radius = circumference / (2 * math.pi)
            return math.pi * radius ** 2
        else:
            return 0.0


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        # Возвращает площадь треугольника
        sides = self.get_sides()
        if len(sides) == 3:
            a, b, c = sides
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            return area
        else:
            return 0.0


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_volume(self):
        # Возвращает объём куба
        if len(self.get_sides()) >= 1:
            a = self.get_sides()[0]
            return a ** 3
        else:
            return 0.0


# Код для проверки
circle1 = Circle((200, 200, 100), 10)  # Цвет: (200, 200, 100), стороны: [10]
cube1 = Cube((222, 35, 130), 6)  # Цвет: (222, 35, 130), стороны: [6] * 12

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Должен измениться
print(circle1.get_color())  # Вывод: [55, 66, 77]

cube1.set_color(300, 70, 15)  # Не должен измениться
print(cube1.get_color())  # Вывод: [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не должен измениться, sides_count=12
print(cube1.get_sides())  # Вывод: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

circle1.set_sides(15)  # Должен измениться, sides_count=1
print(circle1.get_sides())  # Вывод: [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # Вывод: 15

# Проверка объёма (куба):
print(cube1.get_volume())  # Вывод: 216
