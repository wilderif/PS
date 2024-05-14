# BOJ_1417
# 국회의원 선거

def solution():
    def check_biggest(l):
        biggest_index = [0]
        for i in range(1, len(l)):
            if l[i] > l[biggest_index[0]]:
                biggest_index = [i]
            elif l[i] == l[biggest_index[0]]:
                biggest_index.append(i)

        return biggest_index

    n = int(input())
    can_list = list()
    count = 0

    for _ in range(n):
        can_list.append(int(input()))

    while check_biggest(can_list) != [0]:
        if check_biggest(can_list)[0] == 0:
            can_list[check_biggest(can_list)[1]] -= 1
            can_list[0] += 1
            count += 1
        # else:
        #     a = int((can_list[check_biggest(can_list)[0]] - can_list[0]) / 2) + 1
        #     can_list[check_biggest(can_list)[0]] -= a
        #     can_list[0] += a
        #     count += a
        else:
            can_list[check_biggest(can_list)[0]] -= 1
            can_list[0] += 1
            count += 1

    print(count)


if __name__ == "__main__":
    solution()