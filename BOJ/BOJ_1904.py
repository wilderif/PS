# BOJ_1904
# 01타일

def solution():
    n = int(input())
    mem = [0 for _ in range(n + 2)]
    mem[1] = 1
    mem[2] = 2
    for i in range(3, n + 2):
        mem[i] = mem[i - 1] + mem[i - 2]
        mem[i] %= 15746
    print(mem[n])


if __name__ == "__main__":
<<<<<<< HEAD
    solution()
=======
    solution()
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
