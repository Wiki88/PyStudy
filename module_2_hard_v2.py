#Too ancient cipher. Слишком древний шифр. v2
import random
def cipher():
    n = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    inset = random.choice(n)
    return inset

def gen_pass(n):
    result = ""
    for i in range(1,21):
        for j in range(i+1, 21):
            sum_ = i + j
            if n % sum_ == 0:
                result+= f'{i}{j}'
    return result
n = cipher()
if 3 <= n <= 20:
    set = gen_pass(n)
    print('Случайное число' , n , 'Пароль', set)