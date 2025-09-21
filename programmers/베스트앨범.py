# 베스트앨범


def solution(genres, plays):
    genres_dict = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in genres_dict:
            genres_dict[genre]["total"] += play
            genres_dict[genre]["songs"].append((i, play))
        else:
            genres_dict[genre] = {"total": play, "songs": [(i, play)]}

    genres_list = list(genres_dict.values())
    genres_list.sort(key=lambda x: x["total"], reverse=True)

    res = []

    for genre in genres_list:
        if len(genre["songs"]) == 1:
            res.append(genre["songs"][0][0])
        else:
            genre["songs"].sort(key=lambda x: (x[1], -x[0]), reverse=True)
            for i in range(2):
                res.append(genre["songs"][i][0])

    return res
