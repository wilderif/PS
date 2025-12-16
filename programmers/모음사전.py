# 모음사전


def solution(word):
    char_index = "AEIOU"
    cnt = 0
    res = None

    def backtracking(cur):
        nonlocal cnt, res
        if res:
            return
        if cur == word:
            res = cnt
            return
        if len(cur) == 5:
            return

        for c in char_index:
            cnt += 1
            backtracking(cur + c)

    backtracking("")

    return res
