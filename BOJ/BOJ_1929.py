# BOJ_1929
# 소수 구하기

def solution():
    n, m = map(int, input().split())
    arr = [True for _ in range(m + 1)]
    arr[0], arr[1] = False, False
    for i in range(2, m + 1):
        if arr[i] is True:
            j = 2
            while i * j < m + 1:
                arr[i * j] = False
                j += 1
    for i in range(n, m + 1):
        if arr[i] is True:
            print(i)


if __name__ == "__main__":
    solution()
