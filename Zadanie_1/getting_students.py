import os


def open_file():
    while True:
        try:
            filename = input("podaj nazwę pliku z listą studentów: ")
            if not os.path.exists(filename):
                raise FileNotFoundError
        except Exception:
            print("Nie ma takiego pliku. Spróbuj jeszcze raz")
        else:
            return filename


def upload_file(filename):

    with open(filename) as f:
        content = f.readlines()
        sclass = []
        names = []
        surnames = []
        tasks = []
        c_grades = []

        for i in content:
            student = i.split(';')
            sclass.append(student[0])
            names.append(student[1])
            surnames.append(student[2])
            tasks.append(student[3])
            c_grades.append(student[4])

        temp_tasks = []
        for index, element in enumerate(tasks):
            try:
                temp_tasks.append(int(element))
            except ValueError:
                temp_tasks.append(0)
                print(f'Note the error or missing data on the list. Check tasks for student ID {index + 1}')
        tasks = temp_tasks


        temp_c_grades = []
        for index, element in enumerate(c_grades):
            try:
                temp_c_grades.append(int(element))
            except ValueError:
                temp_c_grades.append(0)
                print(f'Note the error or missing data on the list. Check grade for student ID {index+1}')
        c_grades = temp_c_grades

    return sclass, names, surnames, tasks, c_grades
