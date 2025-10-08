# 전화번호_목록


def solution(phone_book):
    phone_book.sort(key=lambda x: len(x), reverse=True)
    phone_set = set()
    for p in phone_book:
        if p in phone_set:
            return False
        tmp = ""
        for c in p:
            tmp += c
            phone_set.add(tmp)

    return True
