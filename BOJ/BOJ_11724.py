# BOJ_11724
# 연결 요소의 개수

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    arr = [[]for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, inp().split())
        arr[a].append(b)
        arr[b].append(a)
    visited = [False] * (n + 1)
    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            cnt += 1
            stack = [i]
            visited[i] = True
            while stack:
                cur = stack.pop()
                for j in arr[cur]:
                    if not visited[j]:
                        visited[j] = True
                        stack.append(j)
    print(cnt)


if __name__ == "__main__":
    main()
