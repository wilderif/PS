# BOJ_1065
# 한수

def solution():
    n = int(input())
    count = 0

    for i in range(1, n+1):
        if i < 100:
            count += 1
        else:
            for j in range(2, len(str(i))):
                if int(str(i)[j]) - int(str(i)[j - 1]) != int(str(i)[j - 1]) - int(str(i)[j - 2]):
                    break
            else:
                count += 1

    print(count)


if __name__ == "__main__":
    solution()
