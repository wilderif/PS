# BOJ_1436
# 영화감독 숌

def solution():
    n = int(input())
    s = 1
    num = 666

    while n != s:
        num += 1
        if "666" in str(num):
            s += 1

    print(num)


if __name__ == "__main__":
    solution()