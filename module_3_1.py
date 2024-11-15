calls = 0

def count_calls(func):
    def wrap(*args, **kwargs):
        global calls
        calls += 1
        return func(*args, **kwargs)
    return wrap


@count_calls
def string_info(string):
    print((len(string), string.upper(), string.lower()))


@count_calls
def is_contains(string, list_to_search):
    for i in list_to_search:
        if string.lower() in i.lower() or i.lower() in string.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
