names = ['Adam', 'Jan', 'Anna']
tasks = [10, 3, 1]
c_grades = [2, 4, 5]
p_grades = [3, 5, 6]
date = ["30 June"]

massage = 'Welcome {},\n\nthis is a kindly reminder that you have {} tasks left to submit before you can graduate.' \
          '\nYour current grade is {} and can increase to {} if you submit all assignments before the due date (30 June 2022).\n '

for name, task, c_grade, p_grade in zip(names, tasks, c_grades, p_grades):
     print(massage.format(name, task, c_grade, p_grade))



