# BOJ_14912
# 숫자 빈도수

def solution():
    n, d = map(int, input().split())

    cnt = 0
    for i in range(1, n + 1):
        for j in str(i):
            if int(j) == d:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
<<<<<<< HEAD
    solution()
=======
    solution()
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
