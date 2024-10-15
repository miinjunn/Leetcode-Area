from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [()]
        for i in range(len(nums), 0, -1):
            result += list(combinations(nums, i))
        return result


if __name__ == '__main__':
    test = Solution()
    nums1 = [1, 2, 3]
    # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    nums2 = [0]
    # Output: [[],[0]]

    print(test.subsets(nums1))
    print(test.subsets(nums2))
