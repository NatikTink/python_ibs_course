"""" Необходимо считать любой текстовый файл на вашем ПК (можно создать новый)
и создать на его основе новый файл, где содержимое будет записано в обратном порядке.
В конце программы вывести на экран оба файла - старый в неизменном виде и новый в обратном порядке.
"""

file1 = open('my_file.txt', 'r', encoding='utf8')
c = file1.readlines()

d = str(c[0:1])
e = str(c[1:2])
f = d[::-1]
g = e[::-1]
h = str(g + f)

file2 = open('my_file_rev.txt', 'w', encoding='utf8')
file2.write(h)
file1.close()
file2.close()

file1 = open('my_file.txt', 'r', encoding='utf8')
print(file1.readlines())
file2 = open('my_file_rev.txt', 'r', encoding='utf8')
print(file2.readlines())
file1.close()
file2.close()

