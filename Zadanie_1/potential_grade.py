def calculate_potential_grades(c_grades):
    p_grades = []
    for grade in c_grades:
        if grade < 6:
            p_grade = grade + 1
            p_grades.append(p_grade)
        else:
            grade = grade
            p_grades.append(grade)
    return p_grades
