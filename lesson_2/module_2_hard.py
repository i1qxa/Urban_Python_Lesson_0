import random

num = random.randrange(3, 20)
first_num = 1
result = ""
while first_num < num:
    second_num = first_num + 1
    while (first_num + second_num) <= num:
        if num % (first_num + second_num) == 0:
            result += str(first_num) + str(second_num)
        second_num += 1
    first_num += 1
print("num: ",num)
print("result", result)
