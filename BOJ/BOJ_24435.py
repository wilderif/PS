# BOJ_24435
# 카드 게임

import sys
import itertools

inp = sys.stdin.readline


def solution():
    n = int(inp())
    bob = list(inp().rstrip())
    alice = list(inp().rstrip())
    goal = min("".join(bob), "".join(reversed(bob)))
    cand = []
    for seq in itertools.permutations(range(n), n):
        tmp = ""
        for i in seq:
            tmp += alice[i]
        cand.append(tmp)
    cand.sort(reverse=True)
    for i in cand:
        if i < goal:
            print(i)
            return
    alice.sort(reverse=True)
    print("".join(alice[:-1]))


def main():
    t = int(inp())
    for _ in range(t):
        solution()


if __name__ == "__main__":
    main()
