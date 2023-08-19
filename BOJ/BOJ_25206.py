# BOJ_25206
# 너의 평정은

def solution():
    grade_table = {
        'A+': 4.5,
        'A0': 4.0,
        'B+': 3.5,
        'B0': 3.0,
        'C+': 2.5,
        'C0': 2.0,
        'D+': 1.5,
        'D0': 1.0,
        'F': 0.0
    }
    total_grade = 0.0
    total_time = 0.0
    for _ in range(20):
        grade = list(input().split())
        if grade[2] != 'P':
            total_time += float(grade[1])
            total_grade += float(grade_table[grade[2]] * float(grade[1]))

    print(total_grade/total_time)


if __name__ == "__main__":
    solution()
