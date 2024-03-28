'''
Есть класс Animal c одним методом voice().
class Animal:
def voice(self):
pass
1. Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().

2. Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().
'''

class Animal:
    def voice(self):
        pass


class Animal_one(Animal):
    def voice(self):
        print("Привет, я Animal_one")


class Animal_two(Animal):
    def voice(self):
        print("Привет, я Animal_two")


class Animal_three(Animal):
    def voice(self):
        print("Привет, я Animal_three")

#Проверить вывод(типа тест):

a = Animal_one()
a.voice()

b = Animal_two()
b.voice()

c = Animal_three()
c.voice()

