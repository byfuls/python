def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(f'a type: {type(a)}')
print(f'b type: {type(b)}')

print(f'a: {a}')
print(f'b: {b}')

print(f'a func call: {a()}')
print(f'b func call: {b()}')