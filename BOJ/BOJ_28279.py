# BOJ_28279
# 덱 2

import sys
from collections import deque
        

def main():
    dq = deque()

    n = int(input())
    for _ in range(n):
        inst = list(map(int, sys.stdin.readline().split()))
        if inst[0] == 1:
            dq.appendleft(inst[1])
        elif inst[0] == 2:
            dq.append(inst[1])
        elif inst[0] == 3:
            if dq:
                print(dq.popleft())
            else:
                print(-1)
        elif inst[0] == 4:
            if dq:
                print(dq.pop())
            else:
                print(-1)
        elif inst[0] == 5:
            print(len(dq))
        elif inst[0] == 6:
            if dq:
                print(0)
            else:
                print(1)
        elif inst[0] == 7:
            if dq:
                print(dq[0])
            else:
                print(-1)
        elif inst[0] == 8:
            if dq:
                print(dq[-1])
            else:
                print(-1)


if __name__ == "__main__":
    main()
