# 주식가격


def solution(prices):
    stack = []
    res = [-1 for _ in range(len(prices))]
    for idx, val in enumerate(prices):
        if stack and val < stack[-1][1]:
            while stack and val < stack[-1][1]:
                pop_idx, _ = stack.pop()
                res[pop_idx] = idx - pop_idx
        stack.append((idx, val))

    while stack:
        pop_idx, _ = stack.pop()
        res[pop_idx] = len(prices) - 1 - pop_idx

    return res
