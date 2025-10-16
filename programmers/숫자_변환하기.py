# 숫자_변환하기


def solution(x, y, n):
    if x == y:
        return 0

    vis = [False for _ in range(y + 1)]
    vis[x] = True
    queue = [x]

    cnt = 0
    while queue:
        cnt += 1
        new_queue = []
        for cur in queue:
            nxt_arr = [cur * 2, cur * 3, cur + n]
            for nxt in nxt_arr:
                if nxt > y:
                    continue
                if vis[nxt]:
                    continue
                if nxt == y:
                    return cnt
                vis[nxt] = True
                new_queue.append(nxt)
        queue = new_queue

    return -1
