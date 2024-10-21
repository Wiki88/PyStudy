#Нули ничто, отрицание недопустимо! Zeros are nothing, negation is unacceptable!
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0
while number < (len(my_list)):
    print(my_list[number])
    number += 1
    if my_list[number] < 0:
        break