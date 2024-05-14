# BOJ_16165
# 걸그룹 마스터 준석이

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    group_mem = {}
    mem_group = {}
    for _ in range(n):
        team = inp().rstrip()
        t = int(inp())
        tmp = [inp().rstrip() for _ in range(t)]
        tmp.sort()
        group_mem[team] = tmp
        for i in tmp:
            mem_group[i] = team
    for _ in range(m):
        target = inp().rstrip()
        if int(inp()):
            print(mem_group[target])
        else:
            print('\n'.join(group_mem[target]))


if __name__ == "__main__":
    main()
