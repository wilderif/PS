# BOJ_14405
# 피카츄

import sys

inp = sys.stdin.readline


def main():
    s = inp().rstrip()
    idx = 0
    while idx < len(s):
        if s[idx] == 'p':
            if idx == len(s) - 1:
                print("NO")
                return
            if s[idx + 1] == 'i':
                idx += 2
            else:
                print("NO")
                return
        elif s[idx] == 'k':
            if idx == len(s) - 1:
                print("NO")
                return
            if s[idx + 1] == 'a':
                idx += 2
            else:
                print("NO")
                return
        elif s[idx] == 'c':
            if idx == len(s) - 1 or idx == len(s) - 2:
                print("NO")
                return
            if s[idx + 1] == 'h' and s[idx + 2] == 'u':
                idx += 3
            else:
                print("NO")
                return
        else:
            print("NO")
            return
    print("YES")
                

if __name__ == "__main__":
    main()
