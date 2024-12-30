from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]*nums[-2]) - (nums[0]*nums[1])


if __name__ == "__main__":
    test = Solution()

    nums1 = [5, 6, 2, 7, 4]
    # Output: 34

    nums2 = [4, 2, 5, 9, 7, 4, 8]
    Output: 64

    print(test.maxProductDifference(nums1))
    print(test.maxProductDifference(nums2))
