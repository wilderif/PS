# 구명보트


def solution(people, limit):
    people.sort(reverse=True)
    res = 0
    idx = 0
    while idx < len(people):
        res += 1
        if idx == len(people) - 1:
            break
        if people[idx] + people[-1] <= limit:
            people.pop()
        idx += 1

    return res
