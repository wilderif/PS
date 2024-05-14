# BOJ_1676
# 팩토리얼 0의 개수

def solution():
    def fac(a):
        if a == 0:
            return 1
        return a * fac(a - 1)

    n = int(input())
    out = 0
    result = str(fac(n))

    for i in range(len(result) - 1, 0, -1):
        if result[i] != '0':
            break
        else:
            out += 1
    print(out)


if __name__ == "__main__":
    solution()