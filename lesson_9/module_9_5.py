class StepValueError(ValueError):
    pass


class IterValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        iter_direction = start - stop
        if step == 0:
            raise StepValueError
        elif start == stop or (iter_direction < 0 and step < 0) or (iter_direction > 0 and step > 0):
            raise IterValueError
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step < 0 and self.pointer < self.stop:
            raise StopIteration()
        elif self.step > 0 and self.pointer > self.stop:
            raise StopIteration()
        else:
            self.pointer += self.step
            return self.pointer - self.step


def create_iterator_or_error(start: int, stop: int, step: int = 1):
    try:
        return Iterator(start, stop, step)
    except StepValueError:
        return 'Шаг указан неверно'
    except IterValueError:
        return 'Ошибка, задан бесконечный итератор'


list_of_iterators = [
    create_iterator_or_error(100, 200, 0),
    create_iterator_or_error(-5, 1),
    create_iterator_or_error(6, 15, 2),
    create_iterator_or_error(5, 1, -1),
    create_iterator_or_error(10, 1)
]

for iter in list_of_iterators:
    if isinstance(iter, str):
        print(iter)
    elif isinstance(iter, Iterator):
        print(list(iter))
