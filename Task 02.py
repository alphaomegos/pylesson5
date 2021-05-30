# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

'''
Как я понял это задание, можно вполне воспользоваться файлом из предыдущего задания.
Я назвал его Text01.txt и он прилгается к этой работе.
'''
file = open("Text01.txt", "r")
Line_Count = 0
Word_Count=0

for Line in file:
    if Line != "\n":
        Line_Count += 1
        f1 = Line.split()
        Word_Count = len(f1)
        print(f'Words in line: {Line_Count} is {str(Word_Count)}')
file.close()

print(f'Total number of lines is: {Line_Count}')