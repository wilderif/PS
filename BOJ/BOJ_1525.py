# BOJ_1525
# 퍼즐

import sys

inp = sys.stdin.readline


def swap(board, idx1, idx2):
    board = list(board)
    board[idx1], board[idx2] = board[idx2], board[idx1]
    return "".join(board)


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    target = "123456780"

    board = [list(map(int, inp().split())) for _ in range(3)]
    board = "".join("".join(map(str, el)) for el in board)
    if board == target:
        return 0

    q = [board]
    vis = set()
    vis.add(q[0])
    cnt = 0

    while q:
        nq = []
        cnt += 1
        for cur in q:
            zero_index = cur.index("0")
            x, y = zero_index // 3, zero_index % 3

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if not (0 <= nx < 3 and 0 <= ny < 3):
                    continue

                nxt = swap(cur, x * 3 + y, nx * 3 + ny)
                if nxt == target:
                    return cnt
                if nxt in vis:
                    continue
                nq.append(nxt)
                vis.add(nxt)
        q = nq

    return -1


if __name__ == "__main__":
    print(main())
