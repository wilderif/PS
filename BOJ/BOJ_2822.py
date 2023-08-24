# BOJ_2822
# 점수 계산

def solution():
    total = 0
    point_list = list()
    index_list = list()

    for i in range(8):
        point_list.append([int(input()), i + 1])

    point_list.sort(reverse=True)

    for i in range(5):
        total += point_list[i][0]
        index_list.append(point_list[i][1])

    index_list.sort()

    print(total)
    for i in range(len(index_list)):
        print(index_list[i], end=' ')


if __name__ == "__main__":
    solution()
