from collections import namedtuple

city = namedtuple('city', 'name country population coordinates')
seoul = city('seoul', 'won', 40.101, (12.34, 56,78))

print(f'seoul: {seoul}')
print(f'seoul.population: {seoul.population}')
print(f'seoul.coordinates: {seoul.coordinates}')
print(f'seoul[1]: {seoul[1]}')