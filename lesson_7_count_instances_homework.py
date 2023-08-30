"""Необходимо дополнить "Практическое задание №6" таким образом, чтобы в конце программы мы вызвали статический метод
родительского класса Animal, который вывел бы нам количество всех созданных экземпляров.
Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3."""
class Animal:

    def voice(self):
        pass

    count = 0

    def __init__(self):
        Animal.count = Animal.count + 1



class Animal_one(Animal):

    def voice(self):
        print("Привет, я Animal_one")


class Animal_two(Animal):

    def voice(self):
        print("Привет, я Animal_two")


class Animal_three(Animal):

    def voice(self):
        print("Привет, я Animal_three")

s1=Animal()
s2=Animal()
s3=Animal()
print("The number of students:",Animal.count)