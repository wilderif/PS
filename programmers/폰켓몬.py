# 폰켓몬


def solution(nums):
    kinds = len(set(nums))
    return kinds if kinds < len(nums) // 2 else len(nums) // 2
