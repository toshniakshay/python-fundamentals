class Human:
    def __init__(self, name):
        if not name:
            raise ValueError("Name is mandatory")
        self.name = name


class Student(Human):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"{self.name} is in {self.house} House"
    ...


class Professor(Human):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"{self.name} is Teaching {self.subject}"
    ...


student = Student('Akshay', 'Green')
print(student)
professor = Professor('JP', 'Java')
print(professor)