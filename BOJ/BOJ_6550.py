# BOJ_6550
# 부분 문자열

import sys

inp = sys.stdin.readline


def main():
    while True:
        try:
            s, t = inp().split()
            p_s, p_t = 0, 0
            while p_t < len(t):
                if s[p_s] == t[p_t]:
                    p_s += 1
                    if p_s == len(s):
                        print("Yes")
                        break
                p_t += 1
            else:
                print("No")
        except:
            break


if __name__ == "__main__":
    main()
