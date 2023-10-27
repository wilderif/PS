# BOJ_4158
# CD

import sys


def solution():
    while True:
        n, m = map(int, sys.stdin.readline().split())
        if n == 0 and m == 0:
            break

        n_arr = [int(sys.stdin.readline()) for _ in range(n)]
        m_arr = [int(sys.stdin.readline()) for _ in range(m)]

        n_idx = 0
        m_idx = 0
        res = 0
        while True:
            if n_idx == n or m_idx == m:
                break
            if n_arr[n_idx] == m_arr[m_idx]:
                res += 1
                if n_idx < n - 2:
                    n_idx += 1
                else:
                    m_idx += 1
            elif n_arr[n_idx] > m_arr[m_idx]:
                m_idx += 1
            else:
                n_idx += 1

        print(res)


if __name__ == "__main__":
    solution()
