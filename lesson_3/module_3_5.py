def get_multiplied_digits(number: int) -> int:
    str_number = str(number)
    first = int(str_number[0])
    if str_number.__len__() > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


print(get_multiplied_digits(40203))
