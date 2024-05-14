# BOJ_2839
# 설탕 배달

def solution():
    n = int(input())
    full_five = n // 5

    for i in range(full_five, -1, -1):
        if (n - i * 5) % 3 == 0:
            print(i + (n - i * 5) // 3)
            break
    else:
        print(-1)


if __name__ == "__main__":
<<<<<<< HEAD
    solution()
=======
    solution()
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
