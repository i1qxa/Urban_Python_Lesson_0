import time
from multiprocessing import Pool

file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
all_data = []


def read_info(*names: str):
    global all_data
    for file_name in names:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file.readlines():
                if line == "":
                    break
                all_data.append(line.strip())


start_reading = time.time()
# read_info(*file_names)

if __name__ == '__main__':
    with Pool(4) as p:
        p.map(read_info, file_names)
    print(f"Чтение заняло: {time.time() - start_reading}")

# print(f"Чтение заняло: {time.time() - start_reading}")
