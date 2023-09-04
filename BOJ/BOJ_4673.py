# BOJ_4673
# 셀프 넘버

def solution():
    num_list = list()
    out_list = list()
    for i in range(1, 10001):
        num_list.append(i)
        out_list.append(i)

    for i in num_list:
        target = i
        for j in range(len(str(i))):
            target += int(str(i)[j])
        if target in out_list:
            out_list.remove(target)

    for i in out_list:
        print(i)


if __name__ == "__main__":
    solution()
