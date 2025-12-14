# k진수에서_소수_개수_구하기


def solution(n, k):
    def convert(n, k):
        digits = []
        while n:
            digits.append(str(n % k))
            n //= k

        return "".join(reversed(digits))

    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        for i in range(3, int(num ** (1 / 2) + 1), 2):
            if num % i == 0:
                return False
        return True

    converted = convert(n, k)
    nums = converted.split("0")

    res = 0
    for num in nums:
        if num and is_prime(int(num)):
            res += 1

    return res
