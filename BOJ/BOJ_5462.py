# BOJ_5462
# POI

import sys

inp = sys.stdin.readline


def main():
    n, t, p = map(int, inp().split())
    arr = [list(map(int, inp().split())) for _ in range(n)]
    point = [0 for _ in range(t)]
    p_point = [{"total_point": 0, "solved": 0, "id": i + 1} for i in range(n)]
    for i in range(n):
        for j in range(t):
            if arr[i][j] == 0:
                point[j] += 1
    for i in range(n):
        for j in range(t):
            if arr[i][j] == 1:
                p_point[i]["total_point"] += point[j]
                p_point[i]["solved"] += 1

    p_point.sort(key=lambda x: (-x["total_point"], -x["solved"], x["id"]))
    for i in range(n):
        if p_point[i]["id"] == p:
            print(p_point[i]["total_point"], i + 1)
            return


if __name__ == "__main__":
    main()
