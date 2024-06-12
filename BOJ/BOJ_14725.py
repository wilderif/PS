# BOJ_14725
# 개미굴

import sys

inp = sys.stdin.readline


def insert(trie, path):
    node = trie
    for d in path:
        if d not in node:
            node[d] = {}
        node = node[d]


def out(node, depth):
    for d in sorted(node.keys()):
        print("--" * depth + d)
        out(node[d], depth + 1)


def main():
    n = int(inp())
    trie = {}
    for _ in range(n):
        path = list(inp().split())
        insert(trie, path[1:])
    out(trie, 0)


if __name__ == "__main__":
    main()
