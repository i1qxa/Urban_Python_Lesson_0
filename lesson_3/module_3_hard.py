def calculate_structure_sum(params) -> int:
    if len(params) == 0:
        return 0
    params = collection_to_list(params)
    param = params[0]
    if isinstance(param, int):
        params.remove(param)
        return param + calculate_structure_sum(params)
    elif isinstance(param, str):
        params.remove(param)
        return len(param) + calculate_structure_sum(params)
    elif isinstance(param, list):
        return calculate_structure_sum(param)
    elif isinstance(param, set):
        return calculate_structure_sum(list(param))
    elif isinstance(param, tuple):
        if len(param) == 0:
            params.remove(param)
            return calculate_structure_sum(list(params))
        return calculate_structure_sum(list(param))
    elif isinstance(param, dict):
        dict_as_list = list()
        dict_as_list.extend(param.keys())
        dict_as_list.extend(param.values())
        return calculate_structure_sum(dict_as_list)


def calculate(smth) -> int:
    result = 0
    for i in range(0, len(smth)):
        result += calculate_structure_sum(smth[i])
    return result


def collection_to_list(collection) -> list:
    if isinstance(collection, (tuple, set, list, int, str)):
        return list(collection)
    elif isinstance(collection, dict):
        lst = list()
        lst.extend(collection.keys())
        lst.extend(collection.values())
        return lst


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate(data_structure))
