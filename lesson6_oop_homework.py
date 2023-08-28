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

