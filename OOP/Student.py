class Student:
    def __init__(self, name):
        self.__name = name

class Professor:
    def __init__(self, name):
        self.__name = name
        self.__student_list = []

    def add_student(self, Student):
        self.__student_list.append(Student)

student1 = Student('Ivan')
student2 = Student('Alex')

proffesor1 = Professor('Petrovich')
proffesor1.add_student(student1)
proffesor1.add_student(student2)