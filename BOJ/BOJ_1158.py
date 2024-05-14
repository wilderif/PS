# BOJ_1158
# 요세푸스 문제

def solution():
    n, k = map(int, input().split())
    c = [i for i in range(1, n + 1)]
    out = []
    idx = 0
    while c:
        idx = (idx + k - 1) % len(c)
        out.append(c.pop(idx))

    print("<", end='')
    for i in range(len(out) - 1):
        print(out[i], end=', ')
    print(out[-1], end='')
    print(">")


if __name__ == "__main__":
    solution()
