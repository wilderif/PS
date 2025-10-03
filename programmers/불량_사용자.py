# 불량_사용자


def solution(user_id, banned_id):
    def match(bid):
        ret = []
        for uid in user_id:
            if len(uid) != len(bid):
                continue
            for i in range(len(bid)):
                if bid[i] == "*":
                    continue
                if bid[i] != uid[i]:
                    break
            else:
                ret.append(uid)

        return ret

    def backtrack(idx, used):
        if idx == len(match_arr):
            res_set.add(tuple(sorted(used)))
            return

        for id in match_arr[idx]:
            if id in used:
                continue
            used.add(id)
            backtrack(idx + 1, used)
            used.remove(id)

        return

    match_arr = []

    for bid in banned_id:
        match_arr.append(match(bid))

    res_set = set()
    backtrack(0, set())

    return len(res_set)
