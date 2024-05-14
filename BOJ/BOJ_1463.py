# BOJ_1463
# 1로 만들기

def solution():
    n = int(input())
    mem = [0 for _ in range(n + 3)]
    mem[2] = 1
    mem[3] = 1

    for i in range(4, n + 1):
        if i % 6 == 0:
            mem[i] = min(mem[i - 1], mem[i // 2], mem[i // 3]) + 1
        elif i % 3 == 0:
            mem[i] = min(mem[i - 1], mem[i // 3]) + 1
        elif i % 2 == 0:
            mem[i] = min(mem[i - 1], mem[i // 2]) + 1
        else:
            mem[i] = mem[i - 1] + 1

    print(mem[n])


if __name__ == "__main__":
    solution()
