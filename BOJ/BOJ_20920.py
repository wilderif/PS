# BOJ_20920
# 영단어 암기는 괴로워

import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    d = {}
    for _ in range(n):
        word = sys.stdin.readline().rstrip()
        if len(word) >= m:
            if word in d:
                d[word][0] += 1
            else:
                d[word] = [1, len(word)]
    
    arr = list(d.items())
    arr.sort(key=lambda x:(-x[1][0], -x[1][1], x[0]))
    for i in arr:
        print(i[0])


if __name__ == "__main__":
    main()
