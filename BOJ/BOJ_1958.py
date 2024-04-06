# BOJ_1958
# LCS 3

import sys


def main():
    string_1 = sys.stdin.readline().rstrip()
    string_2 = sys.stdin.readline().rstrip()
    string_3 = sys.stdin.readline().rstrip()
    arr = [[[0 for _ in range(len(string_3) + 1)] for _ in range(len(string_2) + 1)] for _ in range(len(string_1) + 1)]
    for j in range(1, len(string_1) + 1):
        for i in range(1, len(string_2) + 1):
            for k in range(1, len(string_3) + 1):
                if string_1[j - 1] == string_2[i - 1] == string_3[k - 1]:
                    arr[j][i][k] = arr[j - 1][i - 1][k - 1] + 1
                else:
                    arr[j][i][k] = max(arr[j - 1][i][k], arr[j][i - 1][k], arr[j][i][k - 1])

    print(arr[-1][-1][-1])


if __name__ == "__main__":
    main()
