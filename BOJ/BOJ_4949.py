# BOJ_4949
# 균형잡힌 세상

def solution():
    while True:
        in_string = input()
        if in_string == '.':
            break

        stack = list()

        for i in in_string:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    print("no")
                    break
            elif i == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    print("no")
                    break
        else:
            if len(stack) == 0:
                print("yes")
            else:
                print("no")


if __name__ == "__main__":
    solution()
