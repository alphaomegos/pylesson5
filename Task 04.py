# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

'''
Информация считывается из приложенного файла text04.txt и записывается в NewText04.txt
'''
import codecs
f = codecs.open('Text04.txt', 'r', 'utf_8_sig')
filedata = f.read()
f.close()

newdata = filedata.replace("One", "Один")
newdata = filedata.replace("Two", "Два")
newdata = filedata.replace("Three", "Три")
newdata = filedata.replace("Four", "Четыре")

f = codecs.open('NewText04.txt', 'w', 'utf_8_sig')
f.write(newdata)
f.close()


