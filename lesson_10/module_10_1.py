import threading
from time import sleep, time


def wite_words(word_count, file_name):
    start_time = time()
    with open(file_name, "a", encoding="utf-16") as file:
        for i in range(0, word_count):
            sleep(0.1)
            file.write(f'Акулёнок №{i + 1}\n')
    print(f"Запись в файл заняла: {time() - start_time}")
    print(f"Завершилась запись в файл {file_name}")


print(f"Начало записи в файлы: {time()}")
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
print(f"Окончание записи в файлы: {time()}")

thread1 = threading.Thread(target=wite_words, args=(10, "example5.txt"))
thread2 = threading.Thread(target=wite_words, args=(30, "example6.txt"))
thread3 = threading.Thread(target=wite_words, args=(200, "example7.txt"))
thread4 = threading.Thread(target=wite_words, args=(100, "example8.txt"))
threads_list = [thread1, thread2, thread3, thread4]
print(f"Начало записи в файлы используя потоки: {time()}")
for thread in threads_list:
    thread.start()
    thread.join()
print(f"Окончание записи в файлы используя потоки: {time()}")
