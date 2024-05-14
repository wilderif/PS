# BOJ_12852
# 1로 만들기 2

def solution():
    n = int(input())
    mem = [0 for _ in range(n + 3)]
    mem[2] = 1
    mem[3] = 1

    for i in range(4, n + 1):
        if i % 2 == 0 and i % 3 == 0:
            mem[i] = min(mem[i - 1], mem[int(i / 2)], mem[int(i / 3)]) + 1
        elif i % 3 == 0:
            mem[i] = min(mem[i - 1], mem[int(i / 3)]) + 1
        elif i % 2 == 0:
            mem[i] = min(mem[i - 1], mem[int(i / 2)]) + 1
        else:
            mem[i] = mem[i - 1] + 1

    print(mem[n])
    print(n, end=' ')

    while n != 1:
        if mem[n] == mem[n - 1] + 1:
            n = n - 1
        elif mem[n] == mem[int(n / 2)] + 1 and n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(n / 3)

        print(n, end=' ')


if __name__ == "__main__":
    solution()
