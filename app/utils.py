def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n: int) -> bool:
    return sum([i for i in range(1, n) if n % i == 0]) == n


def is_armstrong(n: int) -> bool:
    num_str = str(n)
    num_len = len(num_str)
    return sum(int(digit) ** num_len for digit in num_str) == n


def sum_of_digits(n: int) -> int:
    return sum(int(digit) for digit in str(n))
