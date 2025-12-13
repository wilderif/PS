# 연속_부분_수열_합의_개수


def solution(elements):
    n = len(elements)

    sum_set = set()
    for i in range(n):
        tmp_sum = 0
        for j in range(i, i + n):
            tmp_sum += elements[j % n]
            sum_set.add(tmp_sum)

    return len(sum_set)
