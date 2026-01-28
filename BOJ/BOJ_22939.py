# BOJ_22939
# 쿠키크루

import sys
import itertools

inp = sys.stdin.readline


def main():
    n = int(inp())
    board = [list(inp().rstrip()) for _ in range(n)]
    start, target = None, None
    j_pos = []
    c_pos = []
    b_pos = []
    w_pos = []
    max_val = (100 + 100) * 4
    j_dist, c_dist, b_dist, w_dist = (
        max_val,
        max_val,
        max_val,
        max_val,
    )

    def get_total_dist(pos, seq):
        ret = 0
        ret += get_dist(start, pos[seq[0]])
        for a, b in zip(seq, seq[1:]):
            ret += get_dist(pos[a], pos[b])
        ret += get_dist(pos[seq[-1]], target)
        return ret

    def get_dist(s, d):
        return abs(s[0] - d[0]) + abs(s[1] - d[1])

    for i in range(n):
        for j in range(n):
            if board[i][j] == "H":
                start = (i, j)
            if board[i][j] == "#":
                target = (i, j)
            if board[i][j] == "J":
                j_pos.append((i, j))
            if board[i][j] == "C":
                c_pos.append((i, j))
            if board[i][j] == "B":
                b_pos.append((i, j))
            if board[i][j] == "W":
                w_pos.append((i, j))

    for seq in itertools.permutations(range(3), 3):
        j_dist = min(j_dist, get_total_dist(j_pos, seq))
        c_dist = min(c_dist, get_total_dist(c_pos, seq))
        b_dist = min(b_dist, get_total_dist(b_pos, seq))
        w_dist = min(w_dist, get_total_dist(w_pos, seq))

    res = None
    cur_min = max_val
    for k, v in {
        "Assassin": j_dist,
        "Healer": c_dist,
        "Mage": b_dist,
        "Tanker": w_dist,
    }.items():
        if v < cur_min:
            cur_min = v
            res = k

    print(res)


if __name__ == "__main__":
    main()
