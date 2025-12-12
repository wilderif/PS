# 캐시


from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cache = deque()

    res = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            res += 1
        else:
            if len(cache) == cacheSize:
                tmp = cache.popleft()
            cache.append(city)
            res += 5

    return res
