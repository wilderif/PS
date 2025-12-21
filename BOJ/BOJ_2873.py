# BOJ_2873
# 롤러코스터

import sys

inp = sys.stdin.readline


def main():
    def traverse(not_to_go):
        stack = [(0, 0, "")]
        dirs = [(1, 0, "D"), (-1, 0, "U"), (0, 1, "R")]
        while stack:
            x, y, cur_path = stack.pop()
            if x == 1 and y == c - 1 and len(cur_path) == c * 2 - 2:
                return cur_path
            for dx, dy, p in dirs:
                if len(cur_path) and (p == "D" or p == "U") and cur_path[-1] != "R":
                    continue
                if len(cur_path) > 1 and p == "R" and (cur_path[-2:] == "RR"):
                    continue
                if len(cur_path) and p == "R" and (cur_path[-1] == "R"):
                    if (x + 1) % 2 != not_to_go[0] or y != not_to_go[1]:
                        continue
                nx, ny = x + dx, y + dy
                if not (0 <= nx < 2 and 0 <= ny < c):
                    continue
                if nx == not_to_go[0] and ny == not_to_go[1]:
                    continue

                stack.append((nx, ny, cur_path + p))

    r, c = map(int, inp().split())
    board = [list(map(int, inp().split())) for _ in range(r)]
    move_right = "R" * (c - 1)
    move_left = "L" * (c - 1)
    move_down = "D" * (r - 1)
    move_up = "U" * (r - 1)

    res = []
    if r % 2:
        is_right = True
        for _ in range(r - 1):
            if is_right:
                res.append(move_right)
            else:
                res.append(move_left)
            res.append("D")
            is_right = not is_right
        else:
            res.append(move_right)
    elif c % 2:
        is_down = True
        for _ in range(c - 1):
            if is_down:
                res.append(move_down)
            else:
                res.append(move_up)
            res.append("R")
            is_down = not is_down
        else:
            res.append(move_down)
    else:
        cur_min = 1000
        not_to_go = None
        for i in range(r):
            for j in range(c):
                if (i + j) % 2 == 0:
                    continue
                if board[i][j] < cur_min:
                    not_to_go = (i, j)
                    cur_min = board[i][j]

        for _ in range(not_to_go[0] // 2):
            res.append(move_right + "D" + move_left + "D")

        res.append(traverse((not_to_go[0] % 2, not_to_go[1])))

        if not_to_go[0] // 2 < r // 2 - 1:
            res.append("D")

        for i in range(not_to_go[0] // 2 + 1, r // 2):
            res.append(move_left + "D" + move_right)
            if i != r // 2 - 1:
                res.append("D")

    print("".join(res))


if __name__ == "__main__":
    main()
