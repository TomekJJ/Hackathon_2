import os


def open_message_file():
    while True:
        try:
            filename = input("podaj nazwę pliku z treścią wiadomości: ")
            if not os.path.exists(filename):
                raise FileNotFoundError
        except Exception:
            print("Nie ma takiego pliku. Spróbuj jeszcze raz")
        else:
            return filename


def upload_message(filename):
    with open(filename) as f:
        message = f.read()

    return message


def generate_message(names, surnames, tasks, c_grades, p_grades, message):
    messages_list = []
    for name, surname, task, c_grade, p_grade in zip(names, surnames, tasks, c_grades, p_grades):
        messages_list.append(message.format(name, surname, task, c_grade, p_grade))

    return messages_list
