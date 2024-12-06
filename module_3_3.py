# Распаковка позиционных параметров. Unpacking positional parameters
def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 2, 3]
values_dict = {'a': 4, 'b': 'string2', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [54.32,'String']
print_params(*values_list2, 42)
