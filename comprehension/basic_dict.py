
### dict comprehension ###

#word = 'letters'
#letter_counts = {letter: word.count(letter) for letter in word}
#print(type(letter_counts))
#print(letter_counts)

#account = {month: 0 for month in range(1,13)}
#print(type(account))    # <class 'dict'>
#print(account)          # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

month = {1: 90, 2:85, 3:107, 4:99, 5:102, 6:75, 7:110, 8:119, 9:90, 10:75, 11:95, 12:130}
print(type(month))    # <class 'dict'>
print(month)          # {1: 90, 2: 85, 3: 107, 4: 99, 5: 102, 6: 75, 7: 110, 8: 119, 9: 90, 10: 75, 11: 95, 12: 130}
wannaDie = {month: money for month, money in month.items() if money >= 100}
print(type(wannaDie))    # <class 'dict'>
print(wannaDie)          # {3: 107, 5: 102, 7: 110, 8: 119, 12: 130}

month = {1: 90, 2:85, 3:107, 4:99, 5:102, 6:75, 7:110, 8:119, 9:90, 10:75, 11:95, 12:130}
print(type(month))    # <class 'dict'>
print(month)          # {1: 90, 2: 85, 3: 107, 4: 99, 5: 102, 6: 75, 7: 110, 8: 119, 9: 90, 10: 75, 11: 95, 12: 130}
wannaDie = {month: "등짝 스매싱" if money >= 100 else "살았다.." for month, money in month.items()}
print(type(wannaDie))    # <class 'dict'>
print(wannaDie)          # {1: '살았다..', 2: '살았다..', 3: '등짝 스매싱', 4: '살았다..', 5: '등짝 스매싱', 6: '살았다..', 7: '등짝 스매싱', 8: '등짝 스매싱', 9: '살았다..', 10: '살았다..', 11: '살았다..', 12: '등짝 스매싱'}
