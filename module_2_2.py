first = int(input ('Введите число (число должно быть целым): '))
second = int(input ('Введите число (число должно быть целым): '))
third = int(input ('Введите число (число должно быть целым): '))
if first == second and first == third:
    print("3")
elif first == second or first == third:
    print('2')
else:
    print (0)