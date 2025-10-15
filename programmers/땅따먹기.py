# 땅따먹기


def solution(land):
    n = len(land)
    m = 4

    for i in range(1, n):
        for j in range(m):
            land[i][j] += max(
                land[i - 1][(j + 1) % 4],
                land[i - 1][(j + 2) % 4],
                land[i - 1][(j + 3) % 4],
            )

    return max(land[-1])
