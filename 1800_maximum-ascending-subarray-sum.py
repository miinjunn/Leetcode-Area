from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        temp = nums[0]
        temp2 = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                temp += nums[i]
            else:
                temp2 = max(temp, temp2)
                temp = nums[i]
        result = max(temp, temp2)
        return result


if __name__ == "__main__":
    test = Solution()

    nums1 = [10, 20, 30, 5, 10, 50]
    # Output: 65

    nums2 = [10, 20, 30, 40, 50]
    # Output: 150

    nums3 = [12, 17, 15, 13, 10, 11, 12]
    # Output: 33

    nums4 = [1, 2, 3, 2, 3, 4]
    # Output: 9

    print(test.maxAscendingSum(nums1))
    print(test.maxAscendingSum(nums2))
    print(test.maxAscendingSum(nums3))
    print(test.maxAscendingSum(nums4))
