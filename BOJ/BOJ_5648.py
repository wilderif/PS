# BOJ_5648
# 역원소 정렬

import sys


def main():
    lines = sys.stdin.readlines()
    num = list()
    for line in lines:
        for n in line.split():
            num.append(int(n[::-1]))
    num = num[1:]
    num.sort()
    for i in num:
        print(i)

    
if __name__ == "__main__":
    main()
