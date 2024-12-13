def custom_write(file_name: str, strings: [str]):
    file = open(file_name, 'a', encoding='utf-8')
    pos = 1
    res = {}
    for string in strings:
        res[(pos, file.tell())] = string
        file.write(f"{string}\n")
        pos += 1
    file.close()
    return res


info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
