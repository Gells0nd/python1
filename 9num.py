def count_unique_characters(word):
    return len(set(word))


input_string = input("Введите строку: ")

words = input_string.split()

for word in words:
    unique_count = count_unique_characters(word)
    print(f"Слово '{word}' содержит {unique_count} уникальных символ(ов).")


# ------------------------------------------------------------------


def count_unique_characters(word: str) -> int:
    """ Функция принимает слово и возвращает количество уникальных символов в нем """
    unique_characters = set(word)
    return len(unique_characters)


def count_unique_characters_in_words(input_string: str) -> None:
    """ Функция принимает строку, разбивает ее на слова и выводит количество уникальных символов в каждом слове. """
    words = input_string.split()
    for word in words:
        unique_count = count_unique_characters(word)
        print(f"Слово '{word}' содержит {unique_count} уникальных символ(ов).")


input_string = input("Введите строку: ")
count_unique_characters_in_words(input_string)
