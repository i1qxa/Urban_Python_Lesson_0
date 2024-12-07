from math import pi
from math import sqrt


class Figure:
    def __init__(self, sides_count: int, colors, *sides):
        self.sides_count = sides_count
        self.__sides = []
        self.__color = []
        self.set_sides(*sides)
        self.init_colors(colors)

    def get_color(self) -> list[int]:
        return self.__color

    def __is_valid_color(self, colors) -> bool:
        return all(range(0, 256).__contains__(color) for color in colors)

    def set_color(self, *colors) -> None:
        if self.__is_valid_color(colors):
            self.__color.clear()
            for color in colors:
                self.__color.append(color)

    def init_colors(self, colors) -> None:
        if self.__is_valid_color(colors):
            self.__color.clear()
            for color in colors:
                self.__color.append(color)

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self) -> list[int]:
        return self.__sides

    def __len__(self):
        length = 0
        for side in self.__sides:
            length += side
        return length

    def set_sides(self, *new_sides) -> None:
        if self.__is_valid_sides(*new_sides):
            self.__sides.clear()
            for side in new_sides:
                self.__sides.append(side)

        elif len(self.__sides) == 0:
            for i in range(0, self.sides_count):
                self.__sides.append(1)


class Circle(Figure):
    def __init__(self, colors, *sides):
        super().__init__(1, colors, sides)

    @property
    def radius(self):
        return super().get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, colors, *sides):
        super().__init__(3, colors, sides)

    def get_square(self):
        p = super().__len__() / 2
        return sqrt(p * (p - self.get_sides[0]) * (p - self.get_sides[1]) * (p - self.get_sides[2]))


class Cube(Figure):
    def __init__(self, colors, *sides):
        self.__sides = []
        self.init_sides(sides)
        super().__init__(12, colors)

    def get_volume(self):
        pass
        return self.get_sides()[0] ** 3

    def set_sides(self, *new_sides) -> None:
        if len(new_sides) == 1:
            self.__sides.clear()
            for i in range(0, 12):
                self.__sides.append(new_sides[0])
        elif len(self.__sides) == 0:
            for i in range(0, 12):
                self.__sides.append(1)

    def init_sides(self, new_sides) -> None:
        if len(new_sides) == 1:
            for i in range(0, 12):
                self.__sides.append(new_sides[0])
        elif len(self.__sides) == 0:
            for i in range(0, 12):
                self.__sides.append(1)

    def get_sides(self) -> list[int]:
        return self.__sides


# circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
#
# cube1 = Cube((222, 35, 130), 6)

triangle1 = Triangle((12,22,33), 3,4,5)

# # Проверка на изменение цветов:
#
# circle1.set_color(55, 66, 77)  # Изменится
#
# print(circle1.get_color())
#
# cube1.set_color(300, 70, 15)  # Не изменится
#
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
#
# cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
#
# print(cube1.get_sides())
#
# circle1.set_sides(15)  # Изменится
#
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
#
# print(len(circle1))
#
# # Проверка объёма (куба):
#
# print(cube1.get_volume())

# Проверка треугольника

print(triangle1.get_sides())
print(triangle1.get_square())

