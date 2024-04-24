# BOJ_4779
# 칸토어 집합

import sys

inp = sys.stdin.readline


def recursion(start, size):
    if size == 1:
        return '-'
    left = start
    right = start + (size // 3) * 2
    return recursion(left, size // 3) + ' ' * (size // 3) + recursion(right, size // 3)
    

def main():
    lines = sys.stdin.readlines()
    for n in lines:
        n = int(n)
        n = 3 ** n
        print(recursion(0, n))


if __name__ == "__main__":
    main()
