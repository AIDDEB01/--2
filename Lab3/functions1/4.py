def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


numbers = [10, 15, 17, 18, 19, 23, 24, 29, 30, 31, 37]


prime_numbers = list(filter(lambda x: is_prime(x), numbers))


print("Prime numbers:", prime_numbers)