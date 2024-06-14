from typing import List


# 闭区间
def upper_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right


if __name__ == '__main__':
    arr = [5, 7, 7, 8, 8, 10]
    idx = upper_bound(arr, 7)
    print(idx)
