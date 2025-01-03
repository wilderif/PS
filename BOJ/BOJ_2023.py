# BOJ_2023
# 신기한 소수

import sys

inp = sys.stdin.readline


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
    

def main():
    n = int(inp())

    def backtracking(digit, curNum):
        if not is_prime(curNum):
            return
        if digit == n:
            print(curNum)
            return
        for i in range(1, 10, 2):
            backtracking(digit + 1, curNum * 10 + i)

    backtracking(1, 2)
    backtracking(1, 3)
    backtracking(1, 5)
    backtracking(1, 7)


if __name__ == "__main__":
    main()
 