# BOJ_2029
# 성냥

import sys

inp = sys.stdin.readline


def main():
    board = [list(inp().rstrip()) + ["."] for _ in range(10)] + [
        ["." for _ in range(11)]
    ]
    check = [[[False for _ in range(4)] for _ in range(4)] for _ in range(2)]
    a = 0
    b = 0

    for i in range(0, 10, 3):
        for j in range(0, 10, 3):
            if board[i][j + 1] == "-":
                check[0][i // 3][j // 3] = True
            else:
                if j != 9:
                    a += 1
            if board[i + 1][j] == "|":
                check[1][i // 3][j // 3] = True
            else:
                if i != 9:
                    a += 1

    def find_square(size):
        ret = 0
        for i in range(4 - size):
            for j in range(4 - size):
                for x in range(i, i + size):
                    if not check[1][x][j]:
                        break
                    if not check[1][x][j + size]:
                        break
                else:
                    for y in range(j, j + size):
                        if not check[0][i][y]:
                            break
                        if not check[0][i + size][y]:
                            break
                    else:
                        ret += 1

        return ret

    for i in range(1, 4):
        b += find_square(i)

    print(a, b)


if __name__ == "__main__":
    main()
