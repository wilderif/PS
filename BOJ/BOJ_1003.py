# BOJ_1003
# 피보나치 함수

def solution():
    fib = [[0, 0] for _ in range(41)]
    fib[0] = [1, 0]
    fib[1] = [0, 1]
    for i in range(2, 41):
        fib[i] = [fib[i - 1][0] + fib[i - 2][0], fib[i - 1][1] + fib[i - 2][1]]

    t = int(input())
    for _ in range(t):
        a = int(input())
        print(fib[a][0], end=' ')
        print(fib[a][1])


if __name__ == "__main__":
    solution()
