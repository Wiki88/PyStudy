# Recursive multiplication of digits. Рекурсивное умножение цифр.

def get_multiplied_digits(number):
    str_number = str(number)
    first_ = int(str_number[0])
    if len(str_number) > 2:
        return first_ * get_multiplied_digits(int(str_number[1:]))
    else:
        return first_

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
