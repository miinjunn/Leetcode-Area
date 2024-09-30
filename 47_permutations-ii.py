from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = set(permutations(nums, len(nums)))
        return result


if __name__ == '__main__':
    test = Solution()
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]

    print(test.permute(nums1))
    print(test.permute(nums2))
