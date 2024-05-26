# BOJ_15312
# 이름 궁합

import sys

inp = sys.stdin.readline


def main():
    data = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    str1 = inp().strip()
    str2 = inp().strip()
    arr = []
    for i in range(len(str1)):
        arr.append(data[ord(str1[i]) - ord('A')])
        arr.append(data[ord(str2[i]) - ord('A')])
    
    while len(arr) > 2:
        tmp = []
        for i in range(len(arr) - 1):
            tmp.append((arr[i] + arr[i + 1]) % 10)
        arr = tmp
    for i in arr:
        print(i, end="")

    
if __name__ == "__main__":
    main()
