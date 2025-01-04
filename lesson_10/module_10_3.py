import random
import threading
import time


class Bank:
    balance = 0
    lock = threading.Lock()

    @staticmethod
    def __get_random_num():
        return random.randint(50, 500)

    def deposit(self):
        for i in range(0, 100):
            dep_value = self.__get_random_num()
            self.balance += dep_value
            time.sleep(0.01)
            print(f"Пополнение: {dep_value}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range(0, 100):
            take_value = self.__get_random_num()
            print(f"Запрос на {take_value}")
            if take_value <= self.balance:
                self.balance -= take_value
                print(f"Снятие: {take_value}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank

th1 = threading.Thread(target=Bank.deposit, args=(bk,))

th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()

th2.start()

th1.join()

th2.join()

print(f'Итоговый баланс: {bk.balance}')
