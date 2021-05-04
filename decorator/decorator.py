
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

# decorator-2
@document_it
def add_ints_2(a, b):
    return a+b

print(f'Decorated function call:', add_ints_2(3,4))
#
## decorator-1
#def add_ints(a, b):
#    return a+b
#print(f'Original function call:', add_ints(1,2))

#cooler_add_ints = document_it(add_ints)
#print(f'Decorated function call:', cooler_add_ints(1,2))
