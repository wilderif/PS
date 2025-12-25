# BOJ_14680
# 효빈이의 과외

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    tmp_n = n
    size = []
    matrix = []
    mod = 1_000_000_007
    while tmp_n:
        x, y = map(int, inp().split())
        tmp = [list(map(int, inp().split())) for _ in range(x)]
        size.append((x, y))
        matrix.append(tmp)
        tmp_n -= 1

    for i in range(n - 1):
        if size[i][1] != size[i + 1][0]:
            print(-1)
            return

    def mul_matrix(size_1, size_2, matrix_1, matrix_2):
        ret = [[0 for _ in range(size_2[1])] for _ in range(size_1[0])]
        for i in range(size_1[0]):
            for j in range(size_2[1]):
                for k in range(size_1[1]):
                    ret[i][j] += matrix_1[i][k] * matrix_2[k][j]
                    ret[i][j] %= mod

        return (size_1[0], size_2[1]), ret

    cur_size = size[0]
    cur_matrix = matrix[0]
    for i in range(1, n):
        cur_size, cur_matrix = mul_matrix(cur_size, size[i], cur_matrix, matrix[i])

    print(sum(sum(i) % mod for i in cur_matrix) % mod)


if __name__ == "__main__":
    main()
