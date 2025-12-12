# 호텔_대실


def solution(book_time):
    arr = [0 for _ in range(24 * 60 + 10)]

    def time_to_minute(s):
        h, m = map(int, s.split(":"))
        return h * 60 + m

    for s, e in book_time:
        start = time_to_minute(s)
        end = time_to_minute(e)
        arr[start] += 1
        arr[end + 10] -= 1

    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    return max(arr)
