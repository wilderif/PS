# 압축


def solution(msg):
    dictionary = {}
    for i in range(ord("Z") - ord("A") + 1):
        dictionary[chr(ord("A") + i)] = i + 1

    res = []
    idx = 0
    while idx < len(msg):
        tmp = ""
        for i in range(idx, len(msg)):
            nxt = tmp + msg[i]
            if nxt in dictionary:
                tmp = nxt
                idx += 1
            else:
                res.append(dictionary[tmp])
                dictionary[nxt] = len(dictionary) + 1
                break
        else:
            res.append(dictionary[tmp])

    return res
