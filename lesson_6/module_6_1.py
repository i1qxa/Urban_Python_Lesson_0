class Plant:
    def __init__(self, name: str, edible: bool):
        self.edible = edible
        self.name = name


class Animal:
    def __init__(self, name: str, alive: bool, fed: bool):
        self.alive = alive
        self.fed = fed
        self.name = name

    def eat(self, food: Plant):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Mammal(Animal):
    def __init__(self, name: str, alive: bool = True, fed: bool = False):
        super().__init__(name, alive, fed)


class Predator(Animal):
    def __init__(self, name: str, alive: bool = True, fed: bool = False):
        super().__init__(name, alive, fed)


class Flower(Plant):
    def __init__(self, name: str, edible: bool = False):
        super().__init__(name, edible)


class Fruit(Plant):
    def __init__(self, name: str, edible: bool = True):
        super().__init__(name, edible)


a1 = Predator('Волк с Уолл-Стрит')

a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')

print(a1.name)

print(p1.name)

print(a1.alive)

print(a2.fed)

a1.eat(p1)

a2.eat(p2)

print(a1.alive)

print(a2.fed)
