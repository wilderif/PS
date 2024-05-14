# BOJ_9375
# 패션왕 신해빈

def solution():
    t = int(input())
    for _ in range(t):
        cloth_list = list()
        count = 1
        n = int(input())
        for _ in range(n):
            cloth_name, cloth_type = input().split()
            for i in cloth_list:
                if i[0] == cloth_type:
                    i.append(cloth_name)
                    break
            else:
                cloth_list.append([cloth_type, cloth_name])
        for i in cloth_list:
            count *= len(i)
        print(count - 1)


if __name__ == "__main__":
    solution()