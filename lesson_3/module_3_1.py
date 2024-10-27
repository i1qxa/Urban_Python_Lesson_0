calls: int = 0


def count_calls():
    global calls
    calls += 1


def string_info(some_string: str) -> tuple:
    count_calls()
    return some_string.__len__(), some_string.upper(), some_string.lower()


def is_contains(some_string: str, some_list: list) -> bool:
    count_calls()
    return [s.lower() for s in some_list].__contains__(some_string.lower())


string_info("Ivan")
is_contains("aBc", ["abc", "ssa", "add"])
string_info("ololo")
is_contains("aa", ["abc", "ssa", "add"])
string_info("pyTHon")
is_contains("t", ["abc", "ssa", "add"])
print(calls)
