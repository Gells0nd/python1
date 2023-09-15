import itertools

negative_numbers_generator = (-i for i in itertools.count(start=1, step=1))

for _ in range(10):
    print(next(negative_numbers_generator))


# Функция-генератор для отрицательных чисел
# def negative_numbers_generator():
#     i = 1
#     while True:
#         yield -i
#         i += 1


# negative_gen = negative_numbers_generator()

# for _ in range(10):
#     print(next(negative_gen))
