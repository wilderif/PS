# BOJ_1963
# 소수 경로

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    prime = [False, False, True] + [True, False] * 5000
    for i in range(3, int(10000 ** (0.5)) + 1, 2):
        if prime[i]:
            n = 2
            while i * n < 10000:
                prime[i * n] = False
                n += 1
    
    t = int(inp())
    for _ in range(t):
        a, b = map(int, inp().split())
        q = deque()
        q.append((a, 0))
        used = set()
        used.add(a)
        while q:
            cur = q.popleft()
            if cur[0] == b:
                print(cur[1])
                break
            cur_num = list(str(cur[0]))
            cur_depth = cur[1]
            for j in range(4):
                next = list(cur_num)
                for i in range(10):
                    next[j] = str(i)
                    next_num = int(''.join(next))
                    if prime[next_num] and next_num > 1000 and next_num not in used:
                        used.add(next_num)
                        q.append((next_num, cur_depth + 1))
        else:
            print("Impossible")


if __name__ == "__main__":
    main()
