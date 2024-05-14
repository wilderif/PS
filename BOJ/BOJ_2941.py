# BOJ_2941
# 크로아티아 알파벳

def solution():
    c_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    in_string = list(input())
    count = 0

    while len(in_string) != 0:
        if len(in_string) >= 2 and in_string[0] + in_string[1] in c_list:
            for _ in range(2):
                in_string.pop(0)
            count += 1
        elif len(in_string) >= 3 and in_string[0] + in_string[1] + in_string[2] in c_list:
            for _ in range(3):
                in_string.pop(0)
            count += 1
        else:
            in_string.pop(0)
            count += 1

    print(count)


if __name__ == "__main__":
    solution()
