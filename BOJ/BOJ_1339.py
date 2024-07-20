# BOJ_1339
# 단어 수학

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = [inp().rstrip() for _ in range(n)]
    dic = {}
    for i in arr:
        for j in range(len(i)):
            if i[j] not in dic:
                dic[i[j]] = 10 ** (len(i) - j) // 10
            else:
                dic[i[j]] += 10 ** (len(i) - j) // 10
    arr2 = list(dic.items())
    arr2.sort(key=lambda x:x[1], reverse=True)
    res = 0
    num = 9
    for i in arr2:
        res += i[1] * num
        num -= 1
    print(res)


if __name__ == "__main__":
    main()
