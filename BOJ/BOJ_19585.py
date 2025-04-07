# BOJ_19585
# 전설

import sys

inp = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end = True

    def search(self, word, nickname_set):
        cur = self.root
        for i in range(min(len(word) - 1, 1000)):
            char = word[i]
            if char not in cur.children:
                return False
            cur = cur.children[char]
            if cur.is_end:
                nickname = word[i + 1 :]
                if nickname in nickname_set:
                    return True
        return False


def main():
    c, n = map(int, inp().split())
    trie = Trie()
    nickname_set = set()

    for _ in range(c):
        trie.insert(inp().strip())
    for _ in range(n):
        nickname_set.add(inp().strip())

    q = int(inp())
    for _ in range(q):
        ret = trie.search(inp().strip(), nickname_set)
        if ret:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
