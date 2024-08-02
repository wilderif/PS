# BOJ_8911
# 거북이

import sys

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        s = inp().strip()
        direction = 0
        coord = [0, 0]
        res = [[0, 0], [0, 0]]
        for c in s:
            if c == 'F':
                if direction == 0:
                    coord[0] += 1
                    res[1][0] = max(res[1][0], coord[0])
                if direction == 1:
                    coord[1] += 1
                    res[1][1] = max(res[1][1], coord[1])
                if direction == 2:
                    coord[0] -= 1
                    res[0][0] = min(res[0][0], coord[0])
                if direction == 3:
                    coord[1] -= 1
                    res[0][1] = min(res[0][1], coord[1])
            if c == 'B':
                if direction == 0:
                    coord[0] -= 1
                    res[0][0] = min(res[0][0], coord[0])
                if direction == 1:
                    coord[1] -= 1
                    res[0][1] = min(res[0][1], coord[1])
                if direction == 2:
                    coord[0] += 1
                    res[1][0] = max(res[1][0], coord[0])
                if direction == 3:
                    coord[1] += 1
                    res[1][1] = max(res[1][1], coord[1])
            if c == 'L':
                direction += 3
                direction %= 4
            if c == 'R':
                direction += 1
                direction %= 4
                            
        print((res[1][0] - res[0][0]) * (res[1][1] - res[0][1]))


if __name__ == "__main__":
    main()
