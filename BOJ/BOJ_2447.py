# BOJ_2447
# 별 찍기 - 10

import sys

inp = sys.stdin.readline


def recursion(n):
    if n == 1:
        return '*'
    star = recursion(n // 3)
    ret = []
    for i in star:
        ret.append(i * 3)
    for i in star:
        ret.append(i + ' ' * (n // 3) + i)
    for i in star:
        ret.append(i * 3)
    return ret
    

def main():
    n = int(inp())
    print('\n'.join(recursion(n)))

        
if __name__ == "__main__":
    main()
