# BOJ_2848
# 알고스팟어

import sys
from collections import deque

inp = sys.stdin.readline


def compare(word_1, word_2, graph, indeg):
    for i in range(min(len(word_1), len(word_2))):
        c1, c2 = word_1[i], word_2[i]
        if c1 != c2:
            if ord(c2) - 97 not in graph[ord(c1) - 97]:
                graph[ord(c1) - 97].add(ord(c2) - 97)
                indeg[ord(c2) - 97] += 1
            break
    else:
        if len(word_1) > len(word_2):
            print("!")
            sys.exit()


def main():
    n = int(inp())
    words = [inp().rstrip() for _ in range(n)]

    to_check = [False for _ in range(26)]
    for i in words:
        for j in i:
            to_check[ord(j) - 97] = True

    graph = [set() for _ in range(26)]
    indeg = [0 for _ in range(26)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            compare(words[i], words[j], graph, indeg)

    q = deque()
    for i in range(26):
        if not indeg[i] and to_check[i]:
            q.append(i)

    res = []
    check = False
    while q:
        if len(q) > 1:
            check = True
        cur = q.popleft()
        res.append(cur)
        for nxt in graph[cur]:
            indeg[nxt] -= 1
            if not indeg[nxt]:
                q.append(nxt)
    
    for i in indeg:
        if i:
            print("!")
            return
    if check:
        print("?")
        return
    for i in res:
        print(chr(i + 97), end='')


if __name__ == "__main__":
    main()
