# BOJ_12904
# A와 B

def solution():
    def flip(string):
        out = ''
        for i in range(len(string) - 1, -1, - 1):
            out += string[i]
        return out

    s = input()
    t = input()

    while len(s) < len(t):
        if t[len(t) - 1] == 'A':
            t = t[:len(t) - 1]
        else:
            t = t[:len(t) - 1]
            t = flip(t)
        if s == t:
            print(1)
            break
        if len(s) >= len(t):
            print(0)
            break


if __name__ == "__main__":
    solution()
