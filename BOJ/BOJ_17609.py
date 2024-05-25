# BOJ_17609
# 회문

import sys

inp = sys.stdin.readline


def check(string, start, end, pass_flag):
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            if pass_flag:
                return 2
            else:
                if (not check(string, start, end - 1, True)) or (not check(string, start + 1, end, True)):
                    return 1
                else:
                    return 2
    else:
        return 0


def main():
    t = int(inp())
    for _ in range(t):
        s = inp().strip()
        print(check(s, 0, len(s) - 1, False))

    
if __name__ == "__main__":
    main()
