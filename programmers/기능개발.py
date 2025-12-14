# 기능개발


def solution(progresses, speeds):
    n = len(progresses)
    remain_days = [0 for _ in range(n)]

    for i in range(n):
        remain_days[i] = (100 - progresses[i] + speeds[i] - 1) // speeds[i]

    cur_max = remain_days[0]
    res = [1]

    for i in range(1, n):
        if remain_days[i] <= cur_max:
            res[-1] += 1
        else:
            res.append(1)
            cur_max = remain_days[i]

    return res
