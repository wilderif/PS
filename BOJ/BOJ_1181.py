# BOJ_1181
# 단어 정렬

def solution():
    n = int(input())
    words = []

    for _ in range(n):
        w = input()
        if w not in words:
            words.append(w)
    
    words = sorted(words, key=lambda x: (len(x), x))

    for i in words:
        print(i)

if __name__ == "__main__":
<<<<<<< HEAD
    solution()
=======
    solution()
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
