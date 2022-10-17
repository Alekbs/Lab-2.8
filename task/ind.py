#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import sys
from datetime import date

def add():
    # Запросить данные о работнике.
    name = input("Фамилия и инициалы? ")
    groop = input("Группа? ")
    marks = []
    for i in range(5):
        marks.append(int(input("Введите оценки по 5 предметам? ")))

    # Создать словарь.
    return {
        'name': name,
        'groop': groop,
        'marks': marks,
    }

def help():
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить работника;")
    print("list - вывод студентов с оценками 4 и 5;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")
    year = date.today().year
    print(year)

def list(students):
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+'.format(
        '-' * 30,
        '-' * 20,
        '-' * 9
    )
    print(line)
    print(
        '| {:^30} | {:^20} | {:^9} |'.format(
            "Ф.И.О.",
            "Группа",
            "Оценки"
        )
    )
    print(line)

    # Вывести данные о всех студентах.
    for idx, student in enumerate(students, 1):
        res = all(int(x) > 3 for x in student['marks'])
        if res:
            print(
                '| {:<30} | {:<20} | {:>7} |'.format(
                    student.get('name', ''),
                    student.get('groop', ''),
                    ','.join(map(str, student['marks']))
                )
            )
        else:
            print("Таких студентов нет")
    print(line)


def main():
    # Список работников.
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            student = add()
            # Добавить словарь в список.
            students.append(student)
            # Отсортировать список в случае необходимости.

            if len(students) > 1:
                students.sort(key=lambda item: sum(student['marks']) / len(student['marks']))

        elif command == 'list':
            list(students)

        elif command == 'help':
            help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
