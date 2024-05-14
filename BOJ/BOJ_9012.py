# BOJ_9012
# 괄호

def solution():
    t = int(input())
    for _ in range(t):
        stack = list()
        case = input()

        for i in case:
            if i == '(':
                stack.append(1)
            elif i == ')':
                if len(stack) == 0:
                    print("NO")
                    break
                else:
                    stack.pop(0)
        else:
            if len(stack) == 0:
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    solution()
