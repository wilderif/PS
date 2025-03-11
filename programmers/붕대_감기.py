# 붕대_감기


def solution(bandage, health, attacks):
    init_health = health
    cur_time = 0

    for el in attacks:
        tmp_time = el[0] - cur_time - 1
        health += tmp_time * bandage[1]
        health += (tmp_time // bandage[0]) * bandage[2]
        if health > init_health:
            health = init_health

        health -= el[1]

        if health <= 0:
            return -1
        cur_time = el[0]

    return health
