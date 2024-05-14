# BOJ_9625
# BABBA

def solution():
    k = int(input())
    mem = [[-1 for _ in range(46)] for _  in range(2)]
    mem[0][0] = 1
    mem[1][0] = 0

    for i in range(1, k + 1):
        mem[0][i] = mem[1][i - 1]
        mem[1][i] = mem[0][i - 1] + mem[1][i - 1]

    print(mem[0][k], end=' ')
    print(mem[1][k])


if __name__ == "__main__":
    solution()
