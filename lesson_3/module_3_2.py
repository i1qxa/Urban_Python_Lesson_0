def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [10, False, 'Bobr']
values_dict = {'a': True, 'b': 13, 'c': 'Пятница'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Ololo', 12.56]
print_params(*values_list_2, 42)
