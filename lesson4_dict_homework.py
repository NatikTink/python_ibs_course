#Есть словарь dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}

#Составить из него новый словарь, содержащий только те элементы, у которых значение больше или равно 3.

dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}

result_dict = {}
for k, v in dict.items():
    if v >= 3:
        result_dict[k] = v
print(result_dict)












