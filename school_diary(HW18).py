import random
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1,5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
    {students_marks[student]}''')

print('''
Список команд: 
1. Добавить оценки ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Удалить/отредактировать данные по оценкам, предметам или ученикам
5. Вывести все оценки определенного ученика
6. Вывести средний балл по каждому предмету определенного ученика
7. Добавить нового ученика
8. Добавить новый предмет
9. Выход из программы
0. Повторно вывести список команд.
''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету: ')
        student = input("Введите имя ученика: ")
        class_ = input("Введите предмет: ")
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику.')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                if marks_count == 0:
                    print(f'{class_} - У ученика нет оценок')
                else:
                    print(f'{class_} - {round(marks_sum/marks_count)}')
            print()
    elif command == 3:
        print("3. Вывести все оценки по всем ученикам.")
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 9:
        print('9. Выход из программы')
        break
    elif command == 4:
        print('''4. Удалить/отредактировать данные по оценкам, предметам или ученикам
        1. Удалить данные:
        1.1. Удалить оценку
        1.2. Удалить предмет
        1.3. Удалить ученика
        
        2. Отредактировать данные:
        2.1. Изменить оценку
        2.2. Изменить название предмета
        2.3. Изменить данные ученика
        
        3. Прекратить редактирование данных''')
        while True:
            command2 = float(input("Выберите действие: "))
            if command2 == 1.1:
                print('Удаление оценки.')
                student = input('Введите имя ученика: ')
                class_ = input('Введите название предмета:')
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    mark = int(input('Введите оценку, которую нужно удалить: '))
                    if mark in students_marks[student][class_]:
                        students_marks[student][class_].remove(mark)
                        print('Оценка удалена.')
                    else:
                        print('Удаляемая оценка отсуствует.')
                else:
                    print('Введены неверные данные.')
            if command2 == 1.2:
                print('Удаление предмета.')
                class_ = input('Введите название предмета: ')
                if class_ in classes:
                    for student_classes in students_marks.values():
                        del student_classes[class_]
                    classes.remove(class_)
                    print("Предмет удален из журнала")
                else:
                    print("Введены неверные данные.")
            if command2 == 1.3:
                print('Удаление ученика.')
                student = input('Введите имя ученика: ')
                if student in students:
                    del students_marks[student]
                    students.remove(student)
                    print('Ученик удален.')
                else:
                    print('Введены неверные данные.')
            if command2 == 2.1:
                print('Изменение оценки.')
                student = input('Введите имя студента: ')
                class_ = input('Введите название предмета: ')
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    mark = int(input('Введите оценку, которую хотите изменить: '))
                    if mark in students_marks[student][class_]:
                        newmark = int(input('Введите новую оценку 1-5: '))
                        if 1 <= newmark <= 5:
                            students_marks[student][class_].remove(mark)
                            students_marks[student][class_].append(newmark)
                            print('Оценка успешно изменена.')
                        else:
                            print('Введена некорректная оценка.')
                    else:
                        print('Такой оценки не существует.')
                else:
                    print('Введены неверные данные.')
            if command2 == 2.2:
                print('Изменение названия предмета.')
                class_ = input('Введите предмет, название которого хотите изменить: ')
                if class_ in classes:
                    newclass = input('Введите новое название предмета: ')
                    for student_classes in students_marks.values():
                        student_classes[newclass] = student_classes[class_]
                        del student_classes[class_]
                    classes.append(newclass)
                    classes.remove(class_)
                    print('Название успешно изменено.')
                else:
                    print('Введены неверные данные.')
            if command2 == 2.3:
                print('Изменение данных ученика.')
                student = input('Введите имя ученика: ')
                if student in students:
                    newname = input('Введите новое имя ученика: ')
                    students_marks[newname] = students_marks.pop(student)
                    students.remove(student)
                    students.append(newname)
                    print('Имя ученика изменено.')
                else:
                    print('Введены неверные данные.')
            if command2 == 3.0:
                print('Завершение редактирования данных')
                break

    elif command == 5:
        print('5. Вывести все оценки определенного ученика' )
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(f'''{student}
            {students_marks[student]}''')
        else:
            print('ОШИБКА: Неверное имя ученика')
        print()
    elif command == 6:
        print('6. Вывести средний балл по каждому предмету определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                if marks_count == 0:
                    print(f'{class_} - У ученика нет оценок')
                else:
                    print(f'{class_} - {round(marks_sum / marks_count)}')
            print()
    elif command == 7:
        print('7. Добавление нового ученика')
        newstudent = input('Введите имя нового ученика: ')
        students.append(newstudent)
        students_marks[newstudent] = {}
        for class_ in classes:
            students_marks[newstudent][class_] = []
        print(f'Ученик {newstudent} успешно добавлен.')

    elif command == 8:
        print('8. Добавить новый предмет')
        newclass = input('Введите название нового предмета: ')
        classes.append(newclass)
        for student_classes in students_marks.values():
            student_classes[newclass] = []
        print(f'Предмет {newclass} успешно добавлен.')

    elif command == 0:
        print('''
        Список команд: 
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить/отредактировать данные по оценкам, предметам или ученикам
        5. Вывести все оценки определенного ученика
        6. Вывести средний балл по каждому предмету определенного ученика
        7. Добавить нового ученика
        8. Добавить новый предмет
        9. Выход из программы
        0. Вывести список команд.
        ''')