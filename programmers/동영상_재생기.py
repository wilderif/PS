# 동영상_재생기


def str_to_num(s):
    h, m = map(int, s.split(":"))
    return h * 60 + m


def solution(video_len, pos, op_start, op_end, commands):
    video_len = str_to_num(video_len)
    pos = str_to_num(pos)
    op_start = str_to_num(op_start)
    op_end = str_to_num(op_end)

    if op_start <= pos < op_end:
        pos = op_end
    for c in commands:
        if c == "next":
            pos += 10
            if pos > video_len:
                pos = video_len
        else:
            pos -= 10
            if pos < 0:
                pos = 0
        if op_start <= pos < op_end:
            pos = op_end

    res_h = str(pos // 60)
    res_m = str(pos % 60)

    if len(res_h) < 2:
        res_h = "0" + res_h
    if len(res_m) < 2:
        res_m = "0" + res_m

    return res_h + ":" + res_m
