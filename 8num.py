original_tuple = (1, 2, 2, 3, 4, 4, 5, 6, 6)

repeated_numbers = []

for num in original_tuple:
    if original_tuple.count(num) > 1 and num not in repeated_numbers:
        repeated_numbers.append(num)

print("Повторяющиеся числа из исходного кортежа:", repeated_numbers)

# ---------------------------------------------------


def get_repeated_num(numbers: tuple) -> list:
    """ Возвращает повторяющиеся числа из исходного кортежа """

    repeated_numbers = []

    for num in numbers:
        if numbers.count(num) > 1 and num not in repeated_numbers:
            repeated_numbers.append(num)

    return repeated_numbers
