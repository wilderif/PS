# BOJ_11039
# Short Phrase

import sys

inp = sys.stdin.readline


def main():
    target = [5, 7, 5, 7, 7]

    while True:
        n = int(inp())
        if n == 0:
            break

        arr = list(len(inp().rstrip()) for _ in range(n))
        for start in range(n):
            section = 0
            idx = start
            tmp = 0
            res = 0
            while idx < n:
                tmp += arr[idx]
                idx += 1

                if tmp < target[section]:
                    continue
                elif tmp == target[section]:
                    section += 1
                    tmp = 0
                else:
                    break

                if section == 5:
                    res = start + 1
                    break

            if res:
                print(res)
                break


if __name__ == "__main__":
    main()
