# Есть список numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

# Вывести все нечетные числа больше 50, используя функцию filter().

numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
def filter_odd_num(x):
    if (x % 2) != 0 and x>50:
        return True
    else:
        return False


print(list(filter(filter_odd_num, numbers)))
