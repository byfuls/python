from collections import namedtuple

city = namedtuple('city', 'name country population coordinates')
seoul = city('seoul', 'won', 40.101, (12.34, 56,78))

# _fields
print(f"city's fields: {city._fields}")

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = city._make(delhi_data)
dict_Delhi = delhi._asdict()
print(f'dict_Delhi: {dict_Delhi}')

for key, value in delhi._asdict().items():
    print(key+':', value)