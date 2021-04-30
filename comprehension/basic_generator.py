
### generator comprehension ###
generator = (number for number in range(1,11))
#print(type(generator))   # <class 'generator'>
#print(generator)         # <generator object <genexpr> at 0x10152c890>
#for var in generator:
#    print(var)
#    # 1
#    # 2
#    # 3
#    # 4
#    # 5
#    # 6
#    # 7
#    # 8
#    # 9
#    # 10

listVar = list(generator)
print(listVar)      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
againVar = list(generator)
print(againVar)     # []
