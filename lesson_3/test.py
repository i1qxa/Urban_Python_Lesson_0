def calculate(params) -> int:
    list(params)
    if len(params) == 0:
        return 0
    param = params[0]
    if isinstance(param, int):
        params.remove(param)
        return param + calculate(params)
    elif isinstance(param, str):
        params.remove(param)
        return len(param) + calculate(params)
    elif isinstance(param, list):
        return calculate(param)
    elif isinstance(param, set):
        return calculate(list(param))
    elif isinstance(param, tuple):
        if len(param) == 0:
            params.remove(param)
            return calculate(list(params))
        return calculate(list(param))
    elif isinstance(param, dict):
        dict_as_list = list()
        dict_as_list.extend(param.keys())
        dict_as_list.extend(param.values())
        return calculate(dict_as_list)


def calculate_structure_sum(data:list) -> int:
    result = 0
    for item in data:
        result += calculate(item)
    return result


sample_data = [
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
