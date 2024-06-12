# BOJ_5446
# 용량 부족

import sys

inp = sys.stdin.readline


def char_to_idx(c):
    c = ord(c)
    if c == 46:
        return 0
    if 48 <= c <= 57:
        return c - 48 + 1
    if 65 <= c <= 90:
        return c - 65 + 1 + 10
    if 97 <= c:
        return c - 97 + 1 + 10 + 26
    

def insert(nxt, check, s):
    global unused
    cur = 1
    for c in s:
        c = char_to_idx(c)
        if nxt[cur][c] == -1:
            nxt[cur][c] = unused
            unused += 1
        cur = nxt[cur][c]

    check[cur][0] = True


def mark(nxt, check, s):
    global unused
    cur = 1
    for c in s:
        c = char_to_idx(c)
        if nxt[cur][c] == -1:
            nxt[cur][c] = unused
            unused += 1
        cur = nxt[cur][c]
        check[cur][1] = True


def erase(nxt, check, done, s):
    global res
    cur = 1
    for c in s:
        c = char_to_idx(c)
        cur = nxt[cur][c]
        if done[cur]:
            return
        if not check[cur][1]:
            done[cur] = True
            break
    res += 1


def main():
    t = int(inp())
    for _ in range(t):
        global unused, res
        unused = 2
        mx = 2000 * 20 + 1
        check = [[False, False] for _ in range(mx)]
        nxt = [[-1 for _ in range(26 + 26 + 10 + 1)] for _ in range(mx)]
        
        n1 = int(inp())
        arr = []
        for _ in range(n1):
            s = inp().rstrip()
            arr.append(s)
            insert(nxt, check, s)

        n2 = int(inp())
        for _ in range(n2):
            s = inp().rstrip()
            mark(nxt, check, s)
        if not n2:
            print(1)
            continue

        done = [False for _ in range(mx)]
        res = 0
        for s in arr:
            erase(nxt, check, done, s)
        print(res)


if __name__ == "__main__":
    main()
