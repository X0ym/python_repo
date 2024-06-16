from typing import List


# 查找最后一个小于等于 target 的数，不存在返回 -1
# 示例：275. H 指数 II
# https://leetcode.cn/problems/h-index-ii/description/

class Solution:
    # 闭区间
    def hIndex1(self, citations: List[int]) -> int:
        # 在区间 [left, right] 内询问
        left = 1
        right = len(citations)
        while left <= right:  # 区间不为空
            # 循环不变量：
            # left-1 的回答一定为「是」
            # right+1 的回答一定为「否」
            mid = (left + right) // 2
            # 引用次数最多的 mid 篇论文，引用次数均 >= mid
            if citations[-mid] >= mid:
                left = mid + 1  # 询问范围缩小到 [mid+1, right]
            else:
                right = mid - 1  # 询问范围缩小到 [left, mid-1]
        # 循环结束后 right 等于 left-1，回答一定为「是」
        # 根据循环不变量，right 现在是最大的回答为「是」的数
        return right

    def hIndex2(self, citations: List[int]) -> int:
        # 在区间 (left, right] 内询问
        left = 0
        right = len(citations)
        while left < right:  # 区间不为空
            # 循环不变量：
            # left 的回答一定为「是」
            # right+1 的回答一定为「否」
            mid = (left + right + 1) // 2  # 保证 mid 在二分区间内
            # 引用次数最多的 mid 篇论文，引用次数均 >= mid
            if citations[-mid] >= mid:
                left = mid  # 询问范围缩小到 (mid, right]
            else:
                right = mid - 1  # 询问范围缩小到 (left, mid-1]
        # 根据循环不变量，left 现在是最大的回答为「是」的数
        return left

    def hIndex3(self, citations: List[int]) -> int:
        # 在区间 (left, right) 内询问
        left = 0
        right = len(citations) + 1
        while left + 1 < right:  # 区间不为空
            # 循环不变量：
            # left 的回答一定为「是」
            # right 的回答一定为「否」
            mid = (left + right) // 2
            # 引用次数最多的 mid 篇论文，引用次数均 >= mid
            if citations[-mid] >= mid:
                left = mid  # 询问范围缩小到 (mid, right)
            else:
                right = mid  # 询问范围缩小到 (left, mid)
        # 根据循环不变量，left 现在是最大的回答为「是」的数
        return left


if __name__ == '__main__':
    s = Solution()
    case = [0, 1, 3, 5, 6]
    ans = s.hIndex3(case)
    print(ans)
