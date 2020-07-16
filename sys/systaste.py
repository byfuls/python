import sys

print(f'sys argv length = {len(sys.argv)}')

argvindex = 0
for val in sys.argv:
    print(f'sys.argv[{argvindex}] = {val}')
    argvindex+=1
