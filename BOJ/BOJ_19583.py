# BOJ_19583
# 싸이버개강총회

import sys

inp = sys.stdin.readline


def main():
    s, e, q = inp().split()
    s = int(s[:2] * 60) + int(s[3:])
    e = int(e[:2] * 60) + int(e[3:])
    q = int(q[:2] * 60) + int(q[3:])

    set_start = set()
    set_res = set()
    while True:
        try:
            time, name = inp().split()
        except:
            break
        
        time = int(time[:2] * 60) + int(time[3:])
        if time <= s:
            set_start.add(name)
        elif e <= time <= q:
            if name in set_start:
                set_res.add(name)
    print(len(set_res))


if __name__ == "__main__":
    main()
