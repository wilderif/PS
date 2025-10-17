# 튜플


def solution(s):
    s_arr = []
    s = list(s[1:-2].split("},"))
    for sp in s:
        s_arr.append(list(map(int, sp[1:].split(","))))
    s_arr.sort(key=lambda x: len(x))

    used = set()
    res = []
    for arr in s_arr:
        for num in arr:
            if num not in used:
                used.add(num)
                res.append(num)
                break

    return res
