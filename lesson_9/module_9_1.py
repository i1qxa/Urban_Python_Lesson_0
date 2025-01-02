def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        try:
            result[function.__name__] = function(int_list)
        except BaseException as exc:
            print(f"Ошибка при попытке применения функции: {function.__name__} к {type(int_list)}\nОшибка: {exc.args}")
    return result


print(apply_all_func([6, 20, 15, 9], max, min, int))

print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
