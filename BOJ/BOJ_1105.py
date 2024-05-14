# BOJ_1105
# 팔

def solution():
    l, r = input().split()
    count = 0
    idx = 0

    if len(l) == len(r):
        while idx < len(l):
            if l[idx] == '8' and r[idx] == '8':
                count += 1
                idx += 1
            elif l[idx] == r[idx]:
                idx += 1
            else:
                break
    print(count)


if __name__ == "__main__":
    solution()