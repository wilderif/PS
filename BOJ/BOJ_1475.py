# BOJ_1475
# 방 번호

def solution():
    n = input()
    most_used = [-1, 0]
    used_six_nine = 0
    num_used = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }

    for i in n:
        num_used[int(i)] += 1

    for i in num_used:
        if i == 6 or i == 9:
            continue
        if num_used[i] > most_used[1]:
            most_used = [i, num_used[i]]

    used_six_nine = num_used[6] + num_used[9]
    if used_six_nine % 2 == 0:
        used_six_nine //= 2
    else:
        used_six_nine = used_six_nine // 2 + 1

    if used_six_nine > most_used[1]:
        print(used_six_nine)
    else:
        print(most_used[1])


if __name__ == "__main__":
    solution()
