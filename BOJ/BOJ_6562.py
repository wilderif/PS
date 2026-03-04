# BOJ_6562
# Etaoin Shrdlu

import sys

inp = sys.stdin.readline


def main():
    while True:
        n = int(inp())
        if n == 0:
            break

        input_string = "".join(list(inp().rstrip("\n") for _ in range(n)))
        diagram = {}
        total = len(input_string) - 1
        for i in range(len(input_string) - 1):
            tmp = input_string[i] + input_string[i + 1]
            diagram[tmp] = diagram.get(tmp, 0) + 1
        res = sorted(diagram.items(), key=lambda x: (-x[1], x[0]))[:5]
        for i in res:
            print(f"{i[0]} {i[1]} {(i[1]/total):.6f}")
        print()


if __name__ == "__main__":
    main()
