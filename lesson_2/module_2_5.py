numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    is_prime = True
    num = numbers[i]
    for j in range(2, num):
        if num % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)
print("Primes: ", primes)
print("Not Primes: ", not_primes)
