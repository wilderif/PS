# BOJ_5667
# Tornado!

import sys

inp = sys.stdin.readline


def main():
    while True:
        try:
            n = int(inp())
        except:
            break
        arr = list(map(int, inp().split()))
        check = []
        cur = 0
        for i in arr:
            if i:
                if cur:
                    check.append(cur)
                    cur = 0
                else:
                    continue
            else:
                cur += 1
        if cur:
            check.append(cur)

        if 1 not in arr:
            print((check[0] + 1) // 2)
            continue

        if not arr[0] and not arr[-1] and len(check) > 1:
            check[0] += check.pop()

        res = 0
        for i in check:
            res += i // 2

        print(res)


if __name__ == "__main__":
    main()
