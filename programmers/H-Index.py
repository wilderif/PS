# H-Index


def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    res = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            res = i + 1
        else:
            break
    return res
