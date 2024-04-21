# BOJ_17103
# 골드바흐 파티션

import sys
inp = sys.stdin.readline


def main():
    max_val = 1000001
    prime_check = [True for _ in range(max_val)]
    prime_check[0] = False
    prime_check[1] = False
    for i in range(2, max_val):
        if prime_check[i]:
            j = 2
            while i * j < max_val:
                prime_check[i * j] = False
                j += 1
    
    t = int(inp())
    for _ in range(t):
        n = int(inp())
        res = 0
        for i in range(2, n // 2 + 1):
            if prime_check[i] and prime_check[n - i]:
                res += 1
        print(res)
    

if __name__ == "__main__":
    main()
