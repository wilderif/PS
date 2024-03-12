# BOJ_5430
# AC

import sys
from collections import deque


def run(p, dq):
    global rotate_check
    for i in p:
        if i == 'R':
            rotate_check = not rotate_check
        else:
            if not dq:
                return "error"
            if rotate_check:
                dq.popleft()
            else:
                dq.pop()
    return dq


def main():
    global rotate_check
    t = int(sys.stdin.readline())
    for _ in range(t):
        p = sys.stdin.readline().rstrip()
        n = int(sys.stdin.readline())
        arr = sys.stdin.readline().rstrip()
        arr = arr[1:len(arr) - 1]
        dq = deque()
        tmp = ""
        if arr:
            for i in range(len(arr)):
                if arr[i] == ',':
                    dq.append(tmp)
                    tmp = ""
                else:
                    tmp += arr[i]
            dq.append(tmp)
        rotate_check = True
        dq = run(p, dq)
        if dq == "error":
            print(dq)
        else:
            res = "["
            if rotate_check:
                for i in dq:
                    res += i + ','
            else:
                for i in range(len(dq) - 1, -1, -1):
                    res += dq[i] + ','
            if res[-1] == ',':
                res = res[:-1]
            res += ']'
            print(res)


if __name__ == "__main__":
    main()
