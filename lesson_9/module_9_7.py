def is_prime(sum_func):
    def wrapper(*args):
        res = sum_func(*args)
        for n in range(2, res):
            if not res % n:
                return res
        print('Это простое число')
        return res

    return wrapper


def sum_three(*args):
    return sum(args)


decorated_sum_three = is_prime(sum_three)

print(decorated_sum_three(2, 3, 6))
