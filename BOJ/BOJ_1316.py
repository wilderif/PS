# BOJ_1316
# 그룹 단어 체커

def solution():
    n = int(input())
    count = 0

    for _ in range(n):
        s = list(input())
        check = list()
        idx = 0

        while idx < len(s):
            if s[idx] not in check:
                check.append(s[idx])
                while idx < len(s) - 1 and s[idx + 1] == s[idx]:
                    idx += 1
                idx += 1
            else:
                break
        else:
            count += 1
    print(count)


if __name__ == "__main__":
    solution()
