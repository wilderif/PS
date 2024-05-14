# BOJ_13699
# 점화식

def solution():
    def t(n):
        if mem[n] != -1:
            return mem[n]
        elif n == 0:
            mem[n] = 1
            return mem[n]
        else:
            a = 0
            for i in range(n):
                a += t(i) * t(n - i - 1)
            mem[n] = a
            return mem[n]

    mem = [-1 for _ in range(40)]

    print(t(int(input())))


if __name__ == "__main__":
<<<<<<< HEAD
    solution()
=======
    solution()
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
