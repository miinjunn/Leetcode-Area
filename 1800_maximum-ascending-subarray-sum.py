from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 2
        temp = nums[0]
        for i in range(1, len(nums)):
            if i > temp:
                temp += i
                result = temp
            else:
                temp = i


if __name__ == "__main__":
    test = Solution()

    nums1 = [10, 20, 30, 5, 10, 50]
    # Output: 65

    nums2 = [10, 20, 30, 40, 50]
    # Output: 150

    nums3 = [12, 17, 15, 13, 10, 11, 12]
    # Output: 33

    print(test.maxAscendingSum(nums1))
    print(test.maxAscendingSum(nums2))
    print(test.maxAscendingSum(nums3))
