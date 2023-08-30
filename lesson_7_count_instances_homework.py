"""Необходимо дополнить "Практическое задание №6" таким образом, чтобы в конце программы мы вызвали статический метод
родительского класса Animal, который вывел бы нам количество всех созданных экземпляров.
Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3."""
class Animal:

    def voice(self):
        pass

    count = 0
    def __init__(self):
        Animal.count += 1

    @staticmethod
    def get_count():
        return Animal.count


class Animal_one(Animal):
    def voice(self):
        print("Привет, я Animal_one")

    def display_count(self):
        return Animal.get_count()

class Animal_two(Animal):
    def voice(self):
        print("Привет, я Animal_two")

    def display_count(self):
        return Animal.get_count()


class Animal_three(Animal):
    def voice(self):
        print("Привет, я Animal_three")

    def display_count(self):
        return Animal.get_count()

#Проверить вывод(типа тест):

a = Animal_one()
a.voice()

b = Animal_two()
b.voice()

c = Animal_three()
c.voice()

print("The number of instances:", c.display_count())
