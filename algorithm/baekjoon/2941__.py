alpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

inputData = input()

for ch in alpa:
    inputData = inputData.replace(ch, '*')

print(len(inputData))