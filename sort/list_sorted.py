
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
ret = sorted(student_objects, key=lambda test: test.age)
print(ret)

###############################################################

from operator import itemgetter, attrgetter
ret = sorted(student_objects, key=attrgetter('age'))
print(ret)

ret = sorted(student_objects, key=attrgetter('grade', 'age'))
print(ret)

###############################################################

ret = sorted(student_objects, key=attrgetter('age'), reverse=True)
print(ret)
