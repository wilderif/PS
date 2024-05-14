# BOJ_1991
# 트리 순회

import sys

inp = sys.stdin.readline


def preorder(tree, node):
    print(node, end="")
    node_idx = ord(node) - 65
    if tree[node_idx][1] != ".":
        preorder(tree, tree[node_idx][1])
    if tree[node_idx][2] != ".":
        preorder(tree, tree[node_idx][2])


def inorder(tree, node):
    node_idx = ord(node) - 65
    if tree[node_idx][1] != ".":
        inorder(tree, tree[node_idx][1])
    print(node, end="")
    if tree[node_idx][2] != ".":
        inorder(tree, tree[node_idx][2])


def postorder(tree, node):
    node_idx = ord(node) - 65
    if tree[node_idx][1] != ".":
        postorder(tree, tree[node_idx][1])
    if tree[node_idx][2] != ".":
        postorder(tree, tree[node_idx][2])
    print(node, end="")


def main():
    n = int(inp())
    tree = [[0, 0, 0] for _ in range(n)]
    for _ in range(n):
        p, lc, rc = inp().split()
        tree[ord(p) - 65][1] = lc
        tree[ord(p) - 65][2] = rc
        if lc != ".":
            tree[ord(lc) - 65][0] = p
        if rc != ".":
            tree[ord(rc) - 65][0] = p
    preorder(tree, "A")
    print()
    inorder(tree, "A")
    print()
    postorder(tree, "A")


if __name__ == "__main__":
    main()
