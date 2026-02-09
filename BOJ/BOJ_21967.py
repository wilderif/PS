# BOJ_21967
# 세워라 반석 위에

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))

    count = {}
    res = 0
    left = 0

    for right in range(n):
        count[arr[right]] = count.get(arr[right], 0) + 1

        while max(count) - min(count) > 2:
            if count[arr[left]] == 1:
                del count[arr[left]]
            else:
                count[arr[left]] -= 1
            left += 1

        res = max(res, right - left + 1)

    print(res)


if __name__ == "__main__":
    main()
