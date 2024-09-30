from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list(permutations(nums, len(nums)))
        return result


if __name__ == '__main__':
    test = Solution()
    nums1 = [1, 2, 3]
    nums2 = [0, 1]
    nums3 = [1]

    print(test.permute(nums1))
    print(test.permute(nums2))
    print(test.permute(nums3))
