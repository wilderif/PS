# BOJ_24891
# 단어 마방진

import sys
import itertools

inp = sys.stdin.readline


def main():
    def check(words):
        for i in range(n):
            for j in range(i + 1, n):
                if words[i][j] != words[j][i]:
                    return False
        return True

    n, l = map(int, inp().split())
    arr = [inp().rstrip() for _ in range(l)]
    arr.sort()

    for seq in itertools.permutations(range(l), n):
        words = [arr[i] for i in seq]
        if check(words):
            for w in words:
                print(w)
            return

    print("NONE")


if __name__ == "__main__":
    main()
