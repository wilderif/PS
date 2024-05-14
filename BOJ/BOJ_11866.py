# BOJ_11866
# 요세푸스 문제 0

def solution():
    n, k = map(int, input().split())
    idx = 0
    circle = list(range(1, n + 1))
    out = list()

    while len(circle) != 0:
        idx = (idx + k - 1) % len(circle)
        out.append(circle.pop(idx))

    out = map(str, out)
    print('<' + ', '.join(out) + '>')


if __name__ == "__main__":
    solution()