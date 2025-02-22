# BOJ_1039
# 교환

import sys

inp = sys.stdin.readline


def swap(s, idx_1, idx_2):
    s = list(s)
    s[idx_1], s[idx_2] = s[idx_2], s[idx_1]
    return "".join(s)


def bfs(n, k):
    queue = [n]
    cnt = 0

    while queue and cnt < k:
        new_queue = []
        used = set()
        for num in queue:
            for i in range(len(num)):
                for j in range(i + 1, len(num)):
                    if i == j:
                        continue
                    if i == 0 and num[j] == "0":
                        continue
                    tmp = swap(num, i, j)
                    if tmp in used:
                        continue
                    used.add(tmp)
                    new_queue.append(tmp)
        queue = new_queue
        if queue:
            cnt += 1

    if cnt < k:
        return -1
    else:
        cur_max = 0
        for num in queue:
            cur_max = max(cur_max, int(num))
        return cur_max


def main():
    n, k = inp().split()
    k = int(k)
    print(bfs(n, k))


if __name__ == "__main__":
    main()
