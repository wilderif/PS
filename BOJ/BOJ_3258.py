# BOJ_3258
# 컴포트

import sys

inp = sys.stdin.readline


def main():
    n, z, m = map(int, inp().split())
    m_set = set(map(int, inp().split())) if m else set()
    for i in range(1, z):
        cur, target = 0, z - 1
        while True:
            cur = (cur + i) % n
            if cur == target:
                print(i)
                return
            if cur == 0:
                break
            if cur + 1 in m_set:
                break


if __name__ == "__main__":
    main()
