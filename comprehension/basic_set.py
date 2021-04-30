
### set comprehension ###
setVar = {number for number in range(1,11) if number % 2 == 0}
print(type(setVar))     # <class 'set'>
print(setVar)           # {2, 4, 6, 8, 10}
