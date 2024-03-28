# Вывести на экран сумму четных чисел от 1 до 100 включительно, используя функцию range()
number = 0
summa = 0
for x in range(2,101,2):
    if x % 2 == 0:
        summa += x
print(summa)
