# BOJ_15645
# 내려가기 2

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    mem_min = [[0 for _ in range(3)] for _ in range(2)]
    mem_max = [[0 for _ in range(3)] for _ in range(2)]
    for _ in range(n):
        arr = list(map(int, inp().split()))
        mem_min[1][0] = min(mem_min[0][:2]) + arr[0]
        mem_min[1][1] = min(mem_min[0]) + arr[1]
        mem_min[1][2] = min(mem_min[0][1:]) + arr[2]
        mem_min[0] = mem_min[1][:]
        mem_max[1][0] = max(mem_max[0][:2]) + arr[0]
        mem_max[1][1] = max(mem_max[0]) + arr[1]
        mem_max[1][2] = max(mem_max[0][1:]) + arr[2]
        mem_max[0] = mem_max[1][:]
    print(max(mem_max[0]), min(mem_min[0]))


if __name__ == "__main__":
    main()
