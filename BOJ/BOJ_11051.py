# BOJ_11051
# 이항 계수 2

def solution():
    n, k = map(int, input().split())

    mem = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(len(mem)):
        mem[i][i] = 1
        mem[i][0] = 1
    for i in range(len(mem)):
        for j in range(1, i):
            mem[i][j] = mem[i - 1][j] + mem[i - 1][j - 1]
            mem[i][j] %= 10007

    print(mem[n][k])


if __name__ == "__main__":
    solution()
