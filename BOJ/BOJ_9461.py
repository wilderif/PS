# BOJ_9461
# 파도반 수열

def solution():
    mem = [1 for _ in range(101)]
    mem[4] = 2
    mem[5] = 2
    for i in range(6, 101):
        mem[i] = mem[i - 1] + mem[i - 5]

    t = int(input())
    for _ in range(t):
        print(mem[int(input())])


if __name__ == "__main__":
    solution()
