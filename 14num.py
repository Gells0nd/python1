def get_positive_sum(numbers: tuple) -> float:
    """ Возвращает сумму положительных чисел в кортеже """
    sum_positive = 0
    iterator = iter(numbers)
    num = next(iterator, None)

    while num is not None:
        if num > 0:
            sum_positive += num
        num = next(iterator, None)

    return sum_positive


numbers = (1, -2, 3, -4, 5, -6, 7, -8, 9)
result = get_positive_sum(numbers)
print(f"Сумма положительных чисел в кортеже: {result}")


# ! Сравнение скорости

# python3 7num.py  0,02s user 0,01s system 87% cpu 0,027 total - 7 номер

# python3 14num.py  0,01s user 0,01s system 85% cpu 0,024 total - 14 Номер

# * Интератор показал результат в 2 раза выше
