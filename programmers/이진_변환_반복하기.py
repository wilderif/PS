# 이진_변환_반복하기


def solution(s):
    def operation(x):
        nonlocal res
        res[0] += 1

        cnt_zero = 0
        cnt_one = 0

        ret = 0
        for i in x:
            if i == "0":
                cnt_zero += 1
            else:
                cnt_one += 1
        res[1] += cnt_zero

        return bin(cnt_one)[2:]

    res = [0, 0]
    while s != "1":
        s = operation(s)

    return res
