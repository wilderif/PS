# BOJ_10733
# 제로

def solution():
    stack = list()
    out = 0
    n = int(input())

    for _ in range(n):
        a = int(input())
        if a == 0:
            stack.pop(len(stack) - 1)
        else:
            stack.append(a)

    for i in stack:
        out += i
    print(out)


if __name__ == "__main__":
<<<<<<< HEAD
    solution()
=======
    solution()
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
