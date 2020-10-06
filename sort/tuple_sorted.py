
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
ret = sorted(student_tuples, key=lambda student: student[2])
print(ret)

###############################################################

from operator import itemgetter, attrgetter
ret = sorted(student_tuples, key=itemgetter(2))
print(ret)

ret = sorted(student_tuples, key=itemgetter(1,2))
print(ret)

###############################################################

ret = sorted(student_tuples, key=itemgetter(2), reverse=True)
print(ret)
