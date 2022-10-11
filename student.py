import random


class Student:
    houses = ['Red', 'Green', 'Yellow']

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Name is not provided')
        self._name = name

    @classmethod
    def get_house(cls, name):
        print(name, 'is in ', random.choice(cls.houses), ' house')

    @classmethod
    def get(cls):
        name = input('Name: ')
        return cls(name)


if __name__ == '__main__':
    student = Student.get()
    print(student.get_house(student.name))
