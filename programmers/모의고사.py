# 모의고사


def solution(answers):
    a = [1, 2, 3, 4, 5]
    a_len = len(a)
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    b_len = len(b)
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c_len = len(c)

    cnt = [[0, i + 1] for i in range(3)]

    for i in range(len(answers)):
        if a[i % a_len] == answers[i]:
            cnt[0][0] += 1
        if b[i % b_len] == answers[i]:
            cnt[1][0] += 1
        if c[i % c_len] == answers[i]:
            cnt[2][0] += 1

    cnt.sort(key=lambda x: x[0], reverse=True)
    res = [cnt[0][1]]
    if cnt[0][0] == cnt[1][0]:
        res.append(cnt[1][1])
        if cnt[1][0] == cnt[2][0]:
            res.append(cnt[2][1])

    return sorted(res)
