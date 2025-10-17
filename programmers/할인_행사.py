# 할인_행사


def solution(want, number, discount):
    def check():
        for i in range(m):
            if cnt_dict.get(want[i], 0) < number[i]:
                return False
        return True

    n = len(discount)
    m = len(want)
    cnt_dict = dict()
    for i in range(10):
        cnt_dict[discount[i]] = cnt_dict.get(discount[i], 0) + 1

    res = 0
    for i in range(10, n):
        if check():
            res += 1
        cnt_dict[discount[i - 10]] -= 1
        cnt_dict[discount[i]] = cnt_dict.get(discount[i], 0) + 1

    if check():
        res += 1

    return res
