numbers = (1, -2, 3, -4, 5, -6, 7, -8, 9)

sum_positive = 0

for num in numbers:
    if num > 0:
        sum_positive += num

print(f'Сумма положительных чисел в кортеже: {sum_positive}')

#  ------------------------------------------------


def get_positive_sum(numbers: tuple) -> float:
    """ Возвращает сумму положительных чисел в кортеже """
    sum_positive = 0

    for num in numbers:
        if num > 0:
            sum_positive += num

    return sum_positive
