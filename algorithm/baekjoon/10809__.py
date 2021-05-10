# 1
word = input()
alpa = list('abcdefghijklmnopqrstuvwxyz')

for x in alpa:
    print(word.find(x))

# 2
word = input()
alpa = list(range(97,123))

for x in alpa:
    print(word.find(chr(x)))