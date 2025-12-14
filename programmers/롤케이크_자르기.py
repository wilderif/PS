# 롤케이크_자르기


def solution(topping):
    left = {}
    right = {}

    for i in topping:
        right[i] = right.get(i, 0) + 1

    res = 0
    for i in topping:
        left[i] = left.get(i, 0) + 1
        if right[i] == 1:
            del right[i]
        else:
            right[i] -= 1

        if len(left) == len(right):
            res += 1

    return res
