# BOJ_9020
# 골드바흐의 추측

import sys
inp = sys.stdin.readline


def main():
    max_val = 10001
    prime_check = [True for _ in range(max_val)]
    prime_check[0], prime_check[1] = False, False
    prime = []
    for i in range(2, max_val // 2 + 1):
        if prime_check[i]:
            prime.append(i)
            j = 2
            while i * j < max_val:
                prime_check[i * j] = False
                j += 1
    
    t = int(inp())
    for _ in range(t):
        n = int(inp())
        res = None
        for i in prime:
            tmp = n - i
            if i > tmp:
                break
            if prime_check[tmp]:
                res = (i, tmp)
        print(*res)


if __name__ == "__main__":
    main()
