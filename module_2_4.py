# Всё не так уж просто. It's not that simple.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

for i in range (2, len(numbers) + 1):
    for g in range (2 , i):
        if i % g == 0 :
            is_prime = False
            not_primes.append(i)
            break
    else:
        primes.append(i)
print(primes)
print(not_primes)