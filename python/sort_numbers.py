# https://www.codewars.com/kata/5174a4c0f2769dd8b1000003
def solution(nums):
    if isinstance(nums, list):
        nums.sort()
        return nums
    return []
