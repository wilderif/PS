# SWEA_1225
# [S/W 문제해결 기본] 7일차 - 암호생성기


from collections import deque


def solution():
    arr = deque(map(int, input().split()))

    while True:
        flag = False
        for i in range(5):
            tmp = arr.popleft()
            tmp -= i + 1
            if tmp <= 0:
                flag = True
                arr.append(0)
            else:
                arr.append(tmp)
            if flag:
                break
        if flag:
            break
    return arr


def main():
    for _ in range(10):
        tc = int(input())
        res = solution()
        print(f"#{tc}", end=" ")
        print(*res)


main()
