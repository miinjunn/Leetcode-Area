from typing import List
from collections import Counter


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        kamus = sorted(nums)
        for i in nums:
            result.append(kamus.index(i))
        return result


if __name__ == "__main__":
    test = Solution()

    nums1 = [8, 1, 2, 2, 3]
    # Output: [4,0,1,1,3]

    nums2 = [6, 5, 4, 8]
    # Output: [2,1,0,3]

    nums3 = [7, 7, 7, 7]
    # Output: [0, 0, 0, 0]

    print(test.smallerNumbersThanCurrent(nums1))
    print(test.smallerNumbersThanCurrent(nums2))
    print(test.smallerNumbersThanCurrent(nums3))
