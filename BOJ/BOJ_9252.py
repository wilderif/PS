# BOJ_9252
# LCS 2

import sys


def main():
    string_1 = sys.stdin.readline().rstrip()
    string_2 = sys.stdin.readline().rstrip()
    arr = [[0 for _ in range(len(string_2) + 1)] for _ in range(len(string_1) + 1)]
    for j in range(1, len(arr)):
        for i in range(1, len(arr[0])):
            if string_1[j - 1] == string_2[i - 1]:
                arr[j][i] = arr[j - 1][i - 1] + 1
            else:
                arr[j][i] = max(arr[j][i - 1], arr[j - 1][i])

    cur = arr[-1][-1]
    cur_idx = [len(string_1), len(string_2)]
    res = ""
    while cur:
        if arr[cur_idx[0] - 1][cur_idx[1]] == cur:
            cur_idx[0] -= 1
        elif arr[cur_idx[0]][cur_idx[1] - 1] == cur:
            cur_idx[1] -= 1
        else:
            res = string_1[cur_idx[0] - 1] + res
            cur_idx[0] -= 1
            cur_idx[1] -= 1
            cur -= 1

    print(arr[-1][-1])
    print(res)


if __name__ == "__main__":
    main()
