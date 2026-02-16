# BOJ_17091
# 단어 시계

import sys

inp = sys.stdin.readline


def main():
    h = int(inp())
    m = int(inp())

    num_to_string = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "quarter",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        21: "twenty one",
        22: "twenty two",
        23: "twenty three",
        24: "twenty four",
        25: "twenty five",
        26: "twenty six",
        27: "twenty seven",
        28: "twenty eight",
        29: "twenty nine",
        30: "half",
    }

    if h == 12 and m > 30:
        h = 0

    if m == 0:
        print(num_to_string[h], "o' clock")
    elif m == 1:
        print(num_to_string[m], "minute past", num_to_string[h])
    elif m < 15:
        print(num_to_string[m], "minutes past", num_to_string[h])
    elif m == 15:
        print(num_to_string[m], "past", num_to_string[h])
    elif m < 30:
        print(num_to_string[m], "minutes past", num_to_string[h])
    elif m == 30:
        print(num_to_string[m], "past", num_to_string[h])
    elif m < 45:
        print(num_to_string[60 - m], "minutes to", num_to_string[h + 1])
    elif m == 45:
        print(num_to_string[60 - m], "to", num_to_string[h + 1])
    elif m < 59:
        print(num_to_string[60 - m], "minutes to", num_to_string[h + 1])
    elif m == 59:
        print(num_to_string[60 - m], "minute to", num_to_string[h + 1])


if __name__ == "__main__":
    main()
