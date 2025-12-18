# 광고_삽입


def solution(play_time, adv_time, logs):
    def format(time):
        h, m, s = time.split(":")
        return int(h) * 60 * 60 + int(m) * 60 + int(s)

    total_time = format(play_time) + 2
    time_table = [0 for _ in range(total_time)]

    for log in logs:
        start, end = log.split("-")
        time_table[format(start)] += 1
        time_table[format(end)] -= 1

    for i in range(1, total_time):
        time_table[i] += time_table[i - 1]

    ad_time = format(adv_time)

    cur = 0
    for i in range(ad_time):
        cur += time_table[i]

    res_time = 0
    cur_max = cur
    for i in range(total_time - ad_time):
        cur -= time_table[i]
        cur += time_table[i + ad_time]
        if cur > cur_max:
            cur_max = cur
            res_time = i + 1

    h, m, s = res_time // 3600, res_time // 60 - (res_time // 3600) * 60, res_time % 60
    res = f"{h:02d}:{m:02d}:{s:02d}"

    return res
