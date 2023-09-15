students = [
    {"имя": "Анна", "математика": 5, "физика": 5},
    {"имя": "Борис", "математика": 4, "физика": 5},
    {"имя": "Виктор", "математика": 5, "физика": 4},
]

for student in students:
    if student["математика"] == 5 and student["физика"] == 5:
        print(f"{student['имя']} имеет оценку 5 по математике и физике.")

#  --------------------------------------------------------


def find_students_with_high_scores(students: list) -> None:
    """ Функция принимает список словарей, представляющих студентов и их оценки, 
        и выводит имена студентов, у которых оценки по математике и физике равны 5 """

    for student in students:
        if student["математика"] == 5 and student["физика"] == 5:
            print(f"{student['имя']} имеет оценку 5 по математике и физике.")


students = [
    {"имя": "Анна", "математика": 5, "физика": 5},
    {"имя": "Борис", "математика": 4, "физика": 5},
    {"имя": "Виктор", "математика": 5, "физика": 4},
]

find_students_with_high_scores(students)