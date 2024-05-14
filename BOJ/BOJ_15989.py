# BOJ_15989
# 1, 2, 3 더하기 4

def solution():
    t = int(input())
    mem = [0 for _ in range(10001)]
    mem[1] = 1
    mem[2] = 2
    mem[3] = 3
    for i in range(4, 10001):
        mem[i] = mem[i - 3] + i // 2 + 1

    for _ in range(t):
        print(mem[int(input())])


if __name__ == "__main__":
    solution()
