# BOJ_10844
# 쉬운 계단 수

def solution():
    n = int(input())
    mem = [[0 for _ in range(11)] for _ in range(n + 1)]
    for i in range(1, 10):
        mem[1][i] = 1
        mem[1][10] += mem[1][i]

    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                mem[i][j] = mem[i - 1][1]
            elif j == 9:
                mem[i][j] = mem[i - 1][8]
            else:
                mem[i][j] = mem[i - 1][j - 1] + mem[i - 1][j + 1]
            mem[i][10] += mem[i][j]

    print(mem[n][10] % 1000000000)


if __name__ == "__main__":
    solution()
