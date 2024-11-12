from typing import List


class Solution:
    # BASIC ------------------------------------------------------
    # def missingNumber(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     for i in range(n+1):
    #         if i not in nums:
    #             return i

    # OPTIMIZE ------------------------------------------------------
    def missingNumber(self, nums: List[int]) -> int:
        total = sum([i for i in range(len(nums)+1)])
        return total - sum(nums)


if __name__ == "__main__":
    test = Solution()

    nums1 = [3, 0, 1]
    # Output: 2

    nums2 = [0, 1]
    # Output: 2

    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    # Output: 8

    print(test.missingNumber(nums1))
    print(test.missingNumber(nums2))
    print(test.missingNumber(nums3))
