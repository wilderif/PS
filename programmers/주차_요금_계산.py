# 주차_요금_계산


def solution(fees, records):
    def str_to_minute(s):
        h, m = s.split(":")
        return int(h) * 60 + int(m)

    def cal_cost(time):
        if time <= fees[0]:
            return fees[1]
        time -= fees[0]
        return fees[1] + (time + fees[2] - 1) // fees[2] * fees[3]

    in_time = {}
    total_time = {}

    for r in records:
        time, num, t = r.split(" ")
        time = str_to_minute(time)
        if t == "IN":
            in_time[num] = time
        else:
            total_time[num] = total_time.get(num, 0) + time - in_time[num]
            del in_time[num]
    out_time = str_to_minute("23:59")
    for num, time in in_time.items():
        total_time[num] = total_time.get(num, 0) + out_time - time

    total_time = sorted(list(total_time.items()), key=lambda x: x[0])
    res = []
    for _, time in total_time:
        res.append(cal_cost(time))

    return res
