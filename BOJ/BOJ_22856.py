# BOJ_22856
# 트리 순회

import sys
sys.setrecursionlimit(100000)

inp = sys.stdin.readline


def inorder(tree, node):
    global res
    if tree[node][0] != -1:
        res += 1
        inorder(tree, tree[node][0])
    if tree[node][1] != -1:
        res += 1
        inorder(tree, tree[node][1])


def right_depth(tree, node):
    if tree[node][1] == -1:
        return 0
    return right_depth(tree, tree[node][1]) + 1


def main():
    n = int(inp())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n):
        c, l, r = map(int, inp().split())
        tree[c].append(l)
        tree[c].append(r)
    global res
    res = 0
    inorder(tree, 1)
    print(res * 2 - right_depth(tree, 1))
    
    
if __name__ == "__main__":
    main()
