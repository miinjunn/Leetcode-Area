from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
        # easies way to solve this xd


if __name__ == "__main__":
    test = Solution()

    nums1 = [3, 4, 5, 1, 2]
    # Output: 1

    nums2 = [4, 5, 6, 7, 0, 1, 2]
    # Output: 0

    nums3 = [11, 13, 15, 17]
    # Output: 11

    print(test.findMin(nums1))
    print(test.findMin(nums2))
    print(test.findMin(nums3))
