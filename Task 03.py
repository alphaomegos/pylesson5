# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

'''
Я программирую под windows 10. Поэтому для работы с русским языком приходится импортировать кодеки
Возможно, на вашей ОС результат может отличаться.
'''

import codecs
with codecs.open("Text03.txt", "r", "utf_8_sig") as f:
    file_content = f.readlines()

Line_Count = 0
Total_Salary = 0
for line in file_content:
    if float(line.split()[1]) > 20000:
        print(line)
    if line != "\n":
        Line_Count += 1
        Total_Salary += float(line.split()[1])

print (f'\nAverage salary is >>> {round(Total_Salary / Line_Count)}')