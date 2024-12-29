from typing import List
from itertools import combinations


class Solution:
    def total_or(self, state: List[int]):
        maks = 0
        for i in state:
            maks |= i
        return maks

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # a,b,c -> ab,ac,bc,a,b,c, abc
        maks = self.total_or(nums)
        # print(f'maks = {maks}')

        result = 0
        result_list = []
        for i in range(1, len(nums)+1):
            kamus = list(combinations(nums, i))
            for i in kamus:
                if self.total_or(i) == maks:
                    result_list.append(i)
                    result += 1

        # print(f'result_list: {result_list}')
        return result


if __name__ == "__main__":
    test = Solution()

    nums1 = [3, 1]
    # Output: 2

    nums2 = [2, 2, 2]
    # Output: 7

    nums3 = [3, 2, 1, 5]
    # Output: 6

    print(test.countMaxOrSubsets(nums1))
    print(test.countMaxOrSubsets(nums2))
    print(test.countMaxOrSubsets(nums3))
