# 뉴스_클러스터링


from collections import Counter


def solution(str1, str2):
    def str_to_set(s):
        s = s.lower()
        arr = []
        for i in range(len(s) - 1):
            tmp = s[i] + s[i + 1]
            if tmp.isalpha():
                arr.append(tmp)

        return Counter(arr)

    set_1 = str_to_set(str1)
    set_2 = str_to_set(str2)

    if len(set_1) == 0 and len(set_2) == 0:
        return 65536

    return int(sum((set_1 & set_2).values()) / sum((set_1 | set_2).values()) * 65536)
