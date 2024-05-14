# BOJ_14400
# 편의점 2

import sys


def solution():
    n = int(sys.stdin.readline())
    x_arr = []
    y_arr = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        x_arr.append(x)
        y_arr.append(y)
    x_arr.sort()
    y_arr.sort()

    # 중앙 값을 사용하면 그 보다 작은 값의 수와 큰 값의 수 같아서
    # 시그마 할 때 중앙 값은 상쇄 됨
    # a, b, c 일 때
    # b - a
    # 0
    # c - b
    # 가 됨으로 결국 b + c만 남음
    # 짝수일 때도 같은 방식으로 생각해보면 
    # n // 2
    # n // 2 - 1
    # 둘의 평균을 사용하는 것이 결국 시그마 결과는 같음
<<<<<<< HEAD

=======
    
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
    # x_med = 0
    # y_med = 0
    # if n % 2 == 1:
    #     x_med = x_arr[n // 2]
    #     y_med = y_arr[n // 2]
    # else:
    #     x_med = (x_arr[n // 2] + x_arr[n // 2 - 1]) / 2
    #     y_med = (y_arr[n // 2] + y_arr[n // 2 - 1]) / 2
    x_med = x_arr[n // 2]
    y_med = y_arr[n // 2]

<<<<<<< HEAD

=======
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
    res = 0
    for i in range(n):
        res += abs(x_arr[i] - x_med)
        res += abs(y_arr[i] - y_med)
    print(res)


if __name__ == "__main__":
    solution()
