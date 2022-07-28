#Напишите программу, удаляющую из текста все слова, содержащие ""абв""

string1 = input('Введите строку, откуда будем исключать "абв": ')
foundStr = 'абв'

words = string1.split(' ')
new_list = []
for word in words:
   if foundStr not in word:
         new_list.append(word)

print('Результат: ',' '.join(new_list))
