
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
ret = sorted(student_tuples, key=lambda student: student[2])
print(ret)

