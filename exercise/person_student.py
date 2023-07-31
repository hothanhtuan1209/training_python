"""
Create class Person and class Student, class Student inherrits from person class
and adds score attribute, compare scores of 2 students
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)

        self.score = score

    def compare_score(self, other):
        return self.score > other.score
    
student_1 = Student('Nam', 6, 7)
student_2 = Student('Hai', 10, 5)

print(student_1.compare_score(student_2))
