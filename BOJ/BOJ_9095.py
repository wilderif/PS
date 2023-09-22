# BOJ_9095
# 1, 2, 3 더하기

def solution():
    n = int(input())
    mem = [0 for _ in range(12)]
    mem[1] = 1
    mem[2] = 2
    mem[3] = 4
    for i in range(4, 12):
        mem[i] = mem[i - 3] + mem[i - 2] + mem[i - 1]

    for _ in range(n):
        print(mem[int(input())])


if __name__ == "__main__":
    solution()
