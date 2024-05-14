# BOJ_1439
# 뒤집기

def solution():
    s = input()
    split_count = 0

    if len(s) == 1:
        print(1)
    else:
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                split_count += 1
        if split_count % 2 == 0:
            print(int(split_count / 2))
        else:
            print(int(split_count / 2) + 1)


if __name__ == "__main__":
    solution()