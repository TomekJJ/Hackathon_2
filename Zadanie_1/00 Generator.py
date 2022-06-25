from getting_students import open_file, upload_file
from generating_massages import open_message_file, upload_message, generate_message
from potential_grade import calculate_potential_grades

def main():
    student_list_filename = open_file()
    sclass, names, surnames, tasks, c_grades = upload_file(student_list_filename)

    p_grades = calculate_potential_grades(c_grades)
    message_filename = open_message_file()
    message = upload_message(message_filename)

    messages_list = generate_message(names, surnames, tasks, c_grades, p_grades, message)

    for student in messages_list:
        print('*********')
        print(student)


if __name__ == '__main__':
    main()
