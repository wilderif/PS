# BOJ_4604
# Steganography

import sys

inp = sys.stdin.readline


def main():
    decode_dict = {
        0: " ",
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P",
        17: "Q",
        18: "R",
        19: "S",
        20: "T",
        21: "U",
        22: "V",
        23: "W",
        24: "X",
        25: "Y",
        26: "Z",
        27: "'",
        28: ",",
        29: "-",
        30: ".",
        31: "?",
    }

    def decode(seq):
        if len(seq) % 5:
            seq.extend([0 for _ in range(5 - len(seq) % 5)])
        ret = ""
        for i in range(0, len(seq), 5):
            val = 0
            for j in range(5):
                val += seq[i + j] * (2 ** (4 - j))
            ret += decode_dict[val]

        return ret

    seq = []
    while True:
        line = inp().rstrip()
        if line == "#":
            break
        if line == "*":
            print(decode(seq))
            seq = []
            continue
        cur_len = 0
        for c in line:
            if c == " ":
                cur_len += 1
            else:
                if cur_len:
                    seq.append(0 if cur_len % 2 else 1)
                    cur_len = 0


if __name__ == "__main__":
    main()
