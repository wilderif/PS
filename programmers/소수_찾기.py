# 소수_찾기


def solution(numbers: str):
    bound = 10000000
    prime = [False, False, True] + [False if i % 2 else True for i in range(bound)]
    for i in range(3, bound):
        if not prime[i]:
            continue
        for j in range(2, bound):
            if i * j >= bound:
                break
            prime[i * j] = False

    numbers = list(numbers)

    n = len(numbers)

    used = [False for _ in range(n)]
    prime_set = set()

    def backtrack(cur):
        print(cur)
        if cur:
            tmp = int(cur)
            if prime[tmp]:
                prime_set.add(tmp)

        for i in range(n):
            if not used[i]:
                used[i] = True
                backtrack(cur + numbers[i])
                used[i] = False

    backtrack("")

    return len(prime_set)
