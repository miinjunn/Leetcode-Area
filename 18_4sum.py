from typing import List
from itertools import combinations


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp = combinations(sorted(nums), 4)
        result = []
        for i in temp:
            if i not in result and sum(i) == target:
                result.append(i)
        return result


if __name__ == "__main__":
    test = Solution()

    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    # Output: [[2,2,2,2]]

    nums3 = [-5, 5, 4, -3, 0, 0, 4, -2]
    target3 = 4
    # Output: [[-5,0,4,5],[-3,-2,4,5]]

    # print(test.fourSum(nums1, target1))
    # print(test.fourSum(nums2, target2))
    print(test.fourSum(nums3, target3))
