# lower_bound 返回最小的满足 nums[i] >= target 的 i
# 如果数组为空，或者所有数都 < target，则返回 len(nums)
# 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
from typing import List


def check(nums: List[int], target: int) -> int:
    pass


# 闭区间写法 [left, right]
# 循环不变量 check(left-1) == false check(right+1) == true
# mid = (left + right) // 2
# 循环退出条件 left+1 == right
# 答案 left 或 right+1
def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        # 循环不变量：
        # nums[left-1] < target
        # nums[right+1] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right]
        else:
            right = mid - 1  # 范围缩小到 [left, mid-1]
    return left  # 或者 right+1


# 左闭右开区间写法 [left, right)
# 循环不变量 check(left-1) == false check(right) == true
# mid = (left + right) // 2
# 循环退出条件 left == right
# 答案 left 或 right
def lower_bound2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)  # 左闭右开区间 [left, right)
    while left < right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    # 退出时，left == right
    return left  # 或者 right


# 开区间写法 (left, right)
# 循环不变量 check(left) == false check(right) == true
# mid = (left + right) // 2
# 循环退出条件 left + 1 == right
# 答案 left+1 或 right
def lower_bound3(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        # 循环不变量：
        # nums[left] < target
        # nums[right] >= target
        if nums[mid] < target:
            left = mid  # 范围缩小到 (mid, right)
        else:
            right = mid  # 范围缩小到 (left, mid)
    return right  # 或者 left+1


"""
bool check(int x) {/* ... */} // 检查x是否满足某种性质

// 区间分成 左半边不满足，右半边满足
// 区间[l, r]被划分成[l, mid]和[mid + 1, r]时使用：
int bsearch_1(int l, int r)
{
    while (l < r)
    {
        int mid = l + r >> 1;
        // check()判断 mid 是否满足性质
        if (check(mid)) r = mid; //满足取左区间
        else l = mid + 1; //不满足取右区间
    }
    return l;
}

// 区间分成 左半边满足，右半边不满足
// 区间[l, r]被划分成[l, mid - 1]和[mid, r]时使用：
int bsearch_2(int l, int r)
{
    while (l < r)
    {
        int mid = l + r + 1 >> 1;
        // check()判断mid是否满足性质
        if (check(mid)) l = mid;//满足取右区间
        else r = mid - 1;//不满足取左区间
    }
    return l;
}
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums, target)  # 选择其中一种写法即可
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        # 如果 start 存在，那么 end 必定存在
        end = lower_bound(nums, target + 1) - 1
        return [start, end]


if __name__ == '__main__':
    s = Solution()
    arr = [5, 7, 7, 8, 8, 10]
    t = 4
    ans = s.searchRange(arr, t)
    print(ans)

    idx = lower_bound2(arr, 1)
    if idx == len(arr):
        print("无解")
    else:
        print(idx)
