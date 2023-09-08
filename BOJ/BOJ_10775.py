# BOJ_10775
# 공항

import sys


def solution():
    g = int(sys.stdin.readline())
    p = int(sys.stdin.readline())
    gi_list = list()
    gate_list = [-1] + [0 for _ in range(1, g + 1)]
    plane_list = [-1] + [0 for _ in range(1, g + 1)]

    for _ in range(p):
        gi_list.append(int(sys.stdin.readline()))

    filled_gate_start = 0
    filled_idx_start = 1

    for i in range(len(gi_list)):
        if gate_list[filled_idx_start] == 1:
            filled_gate_start += 1
            filled_idx_start += 1
        if gi_list[i] - plane_list[gi_list[i]] <= 0:
            break
        for j in range(gi_list[i] - plane_list[gi_list[i]], filled_gate_start, -1):
            plane_list[gi_list[i]] += 1
            if gate_list[j] == 0:
                gate_list[j] = 1
                break
        else:
            break

    count = 0
    for i in gate_list:
        if i == 1:
            count += 1

    print(count)


if __name__ == "__main__":
    solution()
