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
from typing import List


def check(mid: int, nums: List[int]) -> bool:
    pass


def binary_search(l: int, r: int, nums: List[int]) -> int:
    while l < r:
        mid = l + r // 2
        # check()判断 mid 是否满足性质
        if check(mid):
            r = mid  # 满足取左区间
        else:
            l = mid + 1  # 不满足取右区间
    return l
