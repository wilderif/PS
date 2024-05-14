# BOJ_7785
# 회사에 있는 사람

import sys


def main():
    check = set()
    n = int(sys.stdin.readline())
    for _ in range(n):
        name, oper = sys.stdin.readline().split()
        if oper == "enter":
            check.add(name)
        else:
            check.remove(name)
    res = list(check)
    res.sort(reverse=True)
    for i in res:
        print(i)


if __name__ == "__main__":
    main()
