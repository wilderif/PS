# BOJ_15904
# UCPC는 무엇의 약자일까?

def solution():
    upper_list = []
    out = 0
    for i in input():
        if i.isupper():
            upper_list.append(i)
    for i in upper_list:
        if out == 0 and i == 'U':
            out += 1
        elif out == 1 and i == 'C':
            out += 1
        elif out == 2 and i == 'P':
            out += 1
        elif out == 3 and i == 'C':
            print("I love UCPC")
            break
    else:
        print("I hate UCPC")


if __name__ == "__main__":
    solution()
