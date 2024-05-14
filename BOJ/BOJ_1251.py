# BOJ_1251
# 단어 나누기

def solution():
    def swap(w):
        out_word = ""
        for c in range(len(w) - 1, -1, -1):
            out_word += w[c]
        return out_word

    word = input()
    word_list = list()

    for i in range(1, len(word) - 1):
        word_1 = word[:i]
        for j in range(i + 1, len(word)):
            word_2 = word[i:j]
            word_3 = word[j:]
            word_list.append(swap(word_1) + swap(word_2) + swap(word_3))
    word_list.sort()
    print(word_list[0])


if __name__ == "__main__":
    solution()
