import collections
# Person 객체 만들기
Person = collections.namedtuple("Person", 'name age gender')
P1 = Person(name='Jhon', age=28, gender='남')
P2 = Person(name='Sally', age=28, gender='여')
P3 = Person._make(['Tom', 24, '남'])
print(getattr(P1, 'name'))
print(getattr(P2, 'gender'))
print(getattr(P3, 'age'))
print(f'gender:{P3.gender}')
