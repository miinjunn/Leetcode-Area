from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(len(nums) - 1):
            temp = nums[i]
            for j in range(i+1, len(nums)):
                temp *= nums[j]
                result = max(temp, result, nums[j])

        return result


if __name__ == "__main__":
    test = Solution()

    nums = [2, 3, -2, 4]
    # Output: 6

    nums2 = [-2, 0, -1]
    # Output: 0

    print(test.maxProduct(nums))
    print(test.maxProduct(nums2))
