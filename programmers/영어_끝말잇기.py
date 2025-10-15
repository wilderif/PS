# 영어_끝말잇기


def solution(n, words):
    used = set()
    used.add(words[0])
    res = [0, 0]
    for i in range(1, len(words)):
        if words[i] in used or words[i][0] != words[i - 1][-1]:
            cnt = i + 1
            if cnt % n:
                res[0] = cnt % n
                res[1] = cnt // n + 1
            else:
                res[0] = n
                res[1] = cnt // n

            return res
        used.add(words[i])

    return res
