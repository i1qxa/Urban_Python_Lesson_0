first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(key) - len(value) for key, value in zip(first, second) if len(key) != len(value))
second_result = (len(first[index]) == len(second[index]) for index in range(0, len(first)))
print(list(first_result))
print(list(second_result))
