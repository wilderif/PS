# BOJ_10942
# 팰린드롬?

import sys


def solution():
    sys.setrecursionlimit(2000 * 2000)

    def palindrome(s, e):
        if mem[s][e] != -1:
            return mem[s][e]
        else:
            if s == e:
                mem[s][e] = 1
                return mem[s][e]
            elif s + 1 == e:
                if num_list[s] == num_list[e]:
                    mem[s][e] = 1
                else:
                    mem[s][e] = 0
                return mem[s][e]
            elif num_list[s] != num_list[e]:
                mem[s][e] = 0
                return mem[s][e]
            else:
                mem[s][e] = palindrome(s + 1, e - 1)
                return mem[s][e]

    n = int(sys.stdin.readline())
    num_list = [-1] + list(map(int, sys.stdin.readline().split()))
    mem = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    m = int(sys.stdin.readline())
    for _ in range(m):
        start, end = map(int, sys.stdin.readline().split())
        print(palindrome(start, end))


if __name__ == "__main__":
    solution()
