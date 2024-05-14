# BOJ_10026
# 적록색약

import sys
from collections import deque


def main():
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)

    n = int(sys.stdin.readline())
    arr = list()
    vis_1 = [[False for _ in range(n)] for _ in range(n)]
    vis_2 = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        arr.append(sys.stdin.readline().rstrip())

    q_1 = deque()
    q_1.append((0, 0))
    vis_1[0][0] = True
    q_2 = deque()
    q_2.append((0, 0))
    vis_2[0][0] = True

    res_1 = 1
    res_2 = 1
    for j in range(n):
        for i in range(n):
            if not vis_1[j][i]:
                q_1.append((j, i))
                vis_1[j][i] = True
                res_1 += 1
            if not vis_2[j][i]:
                q_2.append((j, i))
                vis_2[j][i] = True
                res_2 += 1
            
            while q_1:
                cur = q_1.popleft()
                cur_color_1 = arr[cur[0]][cur[1]]
                for d in range(4):
                    ny = cur[0] + dy[d]
                    nx = cur[1] + dx[d]
                    if (0 <= ny < n) and (0 <= nx < n):
                        if (arr[ny][nx] == cur_color_1) and not vis_1[ny][nx]:
                            q_1.append((ny, nx))
                            vis_1[ny][nx] = True

            while q_2:
                cur = q_2.popleft()
                cur_color_2 = arr[cur[0]][cur[1]]
                for d in range(4):
                    ny = cur[0] + dy[d]
                    nx = cur[1] + dx[d]
                    if (0 <= ny < n) and (0 <= nx < n):
                        if cur_color_2 == 'B' and arr[ny][nx] == 'B' and not vis_2[ny][nx]:
                            q_2.append((ny, nx))
                            vis_2[ny][nx] = True
                        elif cur_color_2 != 'B' and arr[ny][nx] != 'B' and not vis_2[ny][nx]:
                            q_2.append((ny, nx))
                            vis_2[ny][nx] = True
    
    print(res_1, end=' ')
    print(res_2)


if __name__ == "__main__":
    main()
