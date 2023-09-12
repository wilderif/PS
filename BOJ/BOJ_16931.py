# BOJ_16931
# 겉넓이 구하기

def solution():
    n, m = map(int, input().split())
    p = list()
    for _ in range(n):
        p.append([0] + list(map(int, input().split())) + [0])
    p = [[0 for _ in range(m+2)]] + p + [[0 for _ in range(m+2)]]

    total = n * m * 2
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if p[j][i] > p[j][i - 1]:
                total += p[j][i] - p[j][i - 1]
            if p[j][i] > p[j][i + 1]:
                total += p[j][i] - p[j][i + 1]
            if p[j][i] > p[j - 1][i]:
                total += p[j][i] - p[j - 1][i]
            if p[j][i] > p[j + 1][i]:
                total += p[j][i] - p[j + 1][i]
    print(total)


if __name__ == "__main__":
    solution()
