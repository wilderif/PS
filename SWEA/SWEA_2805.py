# SWEA_2805
# 농작물 수확하기


def solution():
    n = int(input())
    board = [list(input()) for _ in range(n)]
    ret = 0
    for i in range(n // 2):
        row1 = i
        row2 = n - i - 1
        ret += int(board[row1][n // 2])
        ret += int(board[row2][n // 2])
        for j in range(1, i + 1):
            idx1 = n // 2 + j
            idx2 = n // 2 - j
            ret += int(board[row1][idx1])
            ret += int(board[row1][idx2])
            ret += int(board[row2][idx1])
            ret += int(board[row2][idx2])

    ret += sum(map(int, board[n // 2]))
    return ret


def main():
    t = int(input())
    for i in range(t):
        res = solution()
        print(f"#{i + 1} {res}")


main()
