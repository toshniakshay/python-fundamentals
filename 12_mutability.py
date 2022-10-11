from typing import List, Optional


# -------------------------------------------
# bad way
# -------------------------------------------

class Student:
    def __init__(self, name: str, grades: List[int] = []):
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


akshay = Student(name='Akshay')
anam = Student(name='Anam')
akshay.take_exam(90)

print(akshay.grades)
print(anam.grades)


# # -------------------------------------------
# # Good way
# # -------------------------------------------
#
# class Student1:
#     def __init__(self, name: str, grades: Optional[List[int]] = None):
#         self.name = name
#         self.grades = grades or []
#
#     def take_exam(self, result: int):
#         self.grades.append(result)
#
#
# akshay = Student1(name='Akshay')
# anam = Student1(name='Anam')
# akshay.take_exam(90)
#
# print(akshay.grades)
# print(anam.grades)
