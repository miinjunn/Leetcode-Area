from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1) * (nums[-2]-1)


if __name__ == "__main__":
    test = Solution()

    nums1 = [3, 4, 5, 2]
    # Output: 12

    nums2 = [1, 5, 4, 5]
    # Output: 16

    nums3 = [3, 7]
    # Output: 12

    print(test.maxProduct(nums1))
    print(test.maxProduct(nums2))
    print(test.maxProduct(nums3))
