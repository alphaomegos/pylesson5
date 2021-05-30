# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f = open("Text01.txt", "w+")
a = 'Variable for text lines'
while a != '':
    a = input("Please type next line of press enter to exit >>>")
    f.write('\n')
    f.write(a)
f.close() 