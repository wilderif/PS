# BOJ_2635
# 수 이어가기

def solution():
    n = int(input())
    max_count = 0
    max_list = list()

    for i in range(1, n + 1):
        count = 2
        i_list = list()
        i_list.append(n)
        i_list.append(i)
        while True:
            a = i_list[len(i_list) - 2] - i_list[len(i_list) - 1]
            if a < 0:
                break
            else:
                i_list.append(a)
                count += 1
            if count > max_count:
                max_count = count
                max_list = i_list

    print(max_count)
    for i in max_list:
        print(i, end=' ')


if __name__ == "__main__":
<<<<<<< HEAD
    solution()
=======
    solution()
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
