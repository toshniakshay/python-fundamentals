class Student:
    def __init__(self, name, age, dob, standard=1, score=0):
        self.name = name
        self.age = age
        self.dob = dob
        self.standard = standard
        self.score = score

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Name is Mandatory')
        self._name = name

    @property
    def age(self):
        return self._name

    @age.setter
    def age(self, age):
        if not age:
            raise ValueError('Age is compulsory')
        self._age = age

    @property
    def score(self):
        return self._name

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | DoB : {self.dob} | Standard: {self.standard} | Score: {self.score} "


def main():
    print("Welcome to Student management system")
    students_list = []
    while True:
        user_choice = input("Do you want to add student? Y or N")
        if user_choice == 'y' or user_choice == 'Y':
            name = input("Enter Student Name ")
            age = input("Enter Student Age ")
            dob = input("Enter DoB ")
            standard = input("Enter which standard")
            score = input("Enter score")

            try:
                student = Student(name, age, dob, standard, score)
                students_list.append(student)
                print("Student has been added successfully")
            except ValueError:
                print(ValueError)
                restart = input('Do you want to start again? Y ot N')
                if restart == 'Y' or restart == 'y':
                    continue
                else:
                    break
            choice = input("Do you want to Continue? y or n")
            if choice == "y" or choice == "Y":
                continue
            else:
                break
        else:
            break

    print("-------------------------------------")
    print("List of students")
    for student in students_list:
        print("-------------------------------------")
        print(student)
        print("-------------------------------------")
    print("EXIT")


if __name__ == "__main__":
    main()
