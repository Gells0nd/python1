def sum_positive_recursive(numbers, index=0):
    # Базовый случай: если индекс превысил длину кортежа, вернуть 0
    if index >= len(numbers):
        return 0

    # Рекурсивный случай: суммировать положительные числа начиная с текущего индекса
    current_number = numbers[index]
    if current_number > 0:
        return current_number + sum_positive_recursive(numbers, index + 1)
    else:
        return sum_positive_recursive(numbers, index + 1)


numbers = (1, -2, 3, -4, 5, -6, 7, -8, 9)

sum_positive = sum_positive_recursive(numbers)

print(f'Сумма положительных чисел в кортеже: {sum_positive}')
