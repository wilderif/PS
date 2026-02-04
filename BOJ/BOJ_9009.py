# BOJ_9009
# 피보나치

import sys

inp = sys.stdin.readline


def main():
    bound = int(1e9) + 1
    fib = [0, 1]
    while fib[-1] + fib[-2] < bound:
        fib.append(fib[-1] + fib[-2])

    def find(num):
        ret = 0
        for i in fib:
            if i > num:
                break
            ret = i
        return ret

    t = int(inp())
    for _ in range(t):
        n = int(inp())
        res = []
        while True:
            ret = find(n)
            if ret == 0:
                break
            res.append(ret)
            n -= ret
        print(*sorted(res))


if __name__ == "__main__":
    main()
