import threading
import time


class Knight(threading.Thread):
    __start_enemy_amount = 100

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemy_amount = 0
        counter = 0
        while self.__start_enemy_amount - enemy_amount:
            time.sleep(1)
            counter += 1
            enemy_amount += self.power
            print(f"{self.name} сражается {counter} дней(дня), осталось {enemy_amount} воинов.")
        print(f"{self.name} одержал победу спустя {counter} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)

second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
