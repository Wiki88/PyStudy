def gen_pass(n):
    result = ""
    for i in range(1,21):
        for j in range(i+1, 21):
            sum = i + j
            if n % sum == 0:
                result+= f'{i}{j}'
    return result
n = int(input(" Введите число от 3 до 20 "))
if 3 <= n <= 20:
    set = gen_pass(n)
    print('Случайное число' , n , 'Пароль', set)

