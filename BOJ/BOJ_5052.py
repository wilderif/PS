# BOJ_5052
# 전화번호 목록

import sys

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        n = int(inp())
        arr = list(inp().strip() for _ in range(n))

        arr.sort(key=lambda x: len(x))
        check = set()
        end_flag = False
        for i in range(n):
            tmp = ""
            for j in range(len(arr[i])):
                tmp += arr[i][j]
                if tmp in check:
                    print("NO")
                    end_flag = True
                    break
            check.add(tmp)
            if end_flag:
                break
        else:
            print("YES")

    
if __name__ == "__main__":
    main()
