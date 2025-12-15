# n진수_게임


def solution(n, t, m, p):
    DIGITS = "0123456789ABCDEF"

    def convert(num, base):
        if num == 0:
            return "0"
        ret = []
        while num:
            ret.append(DIGITS[num % base])
            num //= base

        return "".join(reversed(ret))

    game_str = ""
    cur_num = 0
    while len(game_str) < t * m:
        game_str += convert(cur_num, n)
        cur_num += 1

    res = ""
    for i in range(p - 1, t * m, m):
        res += game_str[i]

    return res
