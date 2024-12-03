import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed: int, sound=None):
        self._cords = [0, 0, 0]
        self.speed = speed
        self.sound = sound

    def move(self, dx, dy, dz):
        if (new_dz := (self._cords[2] + dz * self.speed)) < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [self._cords[0] + self.speed * dx, self._cords[1] + self.speed * dy, new_dz]

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        print("Sorry, i'm peaceful :)" if self._DEGREE_OF_DANGER < 5 else "Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    def __init__(self, speed: int, sound=None, beak=True):
        super().__init__(speed, sound)
        self.beak = beak

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 5)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * self.speed / 2


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    def __init__(self, speed: int, sound="Click-click-click"):
        super().__init__(speed, sound)


db = Duckbill(10)

print(db.live)

print(db.beak)

db.speak()

db.attack()

db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()

db.lay_eggs()
