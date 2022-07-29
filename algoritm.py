#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данныx


string = input("Введите строку: ")
# count = 1
# for i in range(len(string)-1):
#     if i <= len(string):
#         if string[i] == string[i + 1]:
#             count += 1
#         else:
#             a = string[i]
#             print(count, string[i])
#             count = 1
# print(count,string[i])

result = []

for i in range(0,len(string)-1,2):
    result.append(int(string[i]) * string[i+1])

print(result)
