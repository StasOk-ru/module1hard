# Вам необходимо решить задачу из реальной жизни:
# "школьные учителя устали подсчитывать вручную средний балл каждого ученика,
# поэтому вам предстоит автоматизировать этот процесс":
#
# На вход даны следующие данные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.
# Вывод в консоль:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
# Примечания:
# Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
# Для решения задачи нужно вспомнить функции
# sum, len и др. (подумать самому).
# Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).
#
# Файл с кодом (module1hard.py) прикрепите к домашнему заданию.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sort_stud = sorted(students)

stud_1 = grades[0]
stud_1_aver = sum(stud_1)/len(stud_1)

stud_2 = grades[1]
stud_2_aver = sum(stud_2)/len(stud_2)

stud_3 = grades[2]
stud_3_aver = sum(stud_3)/len(stud_3)

stud_4 = grades[3]
stud_4_aver = sum(stud_4)/len(stud_4)

stud_5 = grades[4]
stud_5_aver = sum(stud_5)/len(stud_5)

aver = [stud_1_aver, stud_2_aver, stud_3_aver, stud_4_aver, stud_5_aver]

dictionary = {sort_stud[0]:aver[0], sort_stud[1]:aver[1],
              sort_stud[2]:aver[2], sort_stud[3]:aver[3], sort_stud[4]:aver[4]}

# print(sort_stud)
# print(aver)
print()
print('Ученик : средний балл')
print(dictionary)

