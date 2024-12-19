# BOJ_1744
# 수 묶기

def solution():
    n = int(input())
    total = 0
    num_list = list()
    for _ in range(n):
        num_list.append(int(input()))

    num_list.sort()
    idx_z = -1
    idx_o = -1
    idx_p = -1

    for i in range(n):
        if num_list[i] <= 0:
            idx_z = i
        elif num_list[i] == 1:
            idx_o = i
        else:
            idx_p = i

    if idx_o == -1:
        num_list_n = num_list[:idx_z + 1]
        num_list_o = num_list[idx_z + 1:idx_o + 1]
        num_list_p = num_list[idx_z + 1:idx_p + 1]
    else:
        num_list_n = num_list[:idx_z + 1]
        num_list_o = num_list[idx_z + 1:idx_o + 1]
        num_list_p = num_list[idx_o + 1:idx_p + 1]

    idx = 0
    while idx < len(num_list_n):
        if idx == len(num_list_n) - 1:
            total += num_list_n[idx]
            idx += 1
        else:
            total += num_list_n[idx] * num_list_n[idx + 1]
            idx += 2

    idx = 0
    while idx < len(num_list_o):
        total += num_list_o[idx]
        idx += 1

    idx = len(num_list_p) - 1
    while idx > - 1:
        if idx == 0:
            total += num_list_p[idx]
            idx -= 1
        else:
            total += num_list_p[idx] * num_list_p[idx - 1]
            idx -= 2

    print(total)


if __name__ == "__main__":
    solution()
