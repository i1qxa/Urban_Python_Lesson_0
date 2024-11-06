data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sample_data = [
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sub_stack = list()


def calculate_structure_sum(data: list) -> int:
    if data.__len__() == 0 and sub_stack.__len__() == 0:
        return 0

    if sub_stack.__len__() != 0:
        item = sub_stack[0]
        if not isinstance(item, int) and not isinstance(item, str) and len(item) == 0:
            sub_stack.remove(item)
            return calculate_structure_sum(data)

    else:
        item = data[0]
    print(item)

    if isinstance(item, int):
        if sub_stack.__len__() > 0:
            sub_stack.remove(item)
        else:
            data.remove(item)
        return item + calculate_structure_sum(data)
    elif isinstance(item, str):
        if sub_stack.__len__() > 0:
            sub_stack.remove(item)
        else:
            data.remove(item)
        return item.__len__() + calculate_structure_sum(data)
    elif isinstance(item, list):
        if sub_stack.__len__() == 0:
            data.remove(item)
        sub_stack.extend(item)
        return calculate_structure_sum(data)
    elif isinstance(item, set):
        if sub_stack.__len__() == 0:
            data.remove(item)
        sub_stack.extend(item)
        return calculate_structure_sum(data)
    elif isinstance(item, dict):
        if sub_stack.__len__() == 0:
            data.remove(item)
        else:
            sub_stack.remove(item)
        sub_stack.extend(item.keys())
        sub_stack.extend(item.values())
        return calculate_structure_sum(data)
    elif isinstance(item, tuple):
        if sub_stack.__len__() == 0:
            data.remove(item)
        sub_stack.extend(list(item))
        return calculate_structure_sum(data)


print(f"Result: {calculate_structure_sum(sample_data)}")
