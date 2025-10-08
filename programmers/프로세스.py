# 프로세스

from collections import deque


def solution(priorities, location):
    queue = deque([(i, priorities[i]) for i in range(len(priorities))])
    cnt = 0
    while queue:
        cnt += 1
        max_idx = 0
        max_val = 0
        for i in range(len(queue)):
            if queue[i][1] > max_val:
                max_val = queue[i][1]
                max_idx = i

        for i in range(max_idx):
            queue.append(queue.popleft())

        e = queue.popleft()
        if e[0] == location:
            return cnt
