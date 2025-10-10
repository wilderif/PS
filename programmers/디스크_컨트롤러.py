# 디스크_컨트롤러

import heapq


def solution(jobs):
    jobs = [(job[1], job[0], idx) for idx, job in enumerate(jobs)]
    jobs.sort(key=lambda x: x[1], reverse=True)
    cur_time = jobs[-1][1]

    heap = []
    turnaround_time = [-1 for _ in range(len(jobs))]

    while jobs or heap:
        while jobs and jobs[-1][1] <= cur_time:
            heapq.heappush(heap, jobs.pop())

        if heap:
            time, start, idx = heapq.heappop(heap)
            cur_time += time
            turnaround_time[idx] = cur_time - start
        else:
            cur_time = jobs[-1][1]

    return sum(turnaround_time) // len(turnaround_time)
