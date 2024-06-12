# BOJ_7432
# 디스크 트리

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
        print(" " * depth + d)
        out(node[d], depth + 1)


def main():
    n = int(inp())
    trie = {}
    for _ in range(n):
        path = inp().rstrip().split('\\')
        insert(trie, path)
    out(trie, 0)


if __name__ == "__main__":
    main()
