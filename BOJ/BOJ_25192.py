# BOJ_25192
# 인사성 밝은 곰곰이

import sys


def main():
    n = int(sys.stdin.readline())
    dic = set()
    res  = 0
    for _ in range(n):
        s = sys.stdin.readline().rstrip()
        if s == "ENTER":
            dic.clear()
        else:
            if s not in dic:
                res += 1
                dic.add(s)
    print(res)


if __name__ == "__main__":
    main()
