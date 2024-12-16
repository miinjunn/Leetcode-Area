from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            temp = min(nums)
            nums[nums.index(temp)] = temp * multiplier
        return nums


if __name__ == "__main__":
    test = Solution()

    nums1 = [2, 1, 3, 5, 6]
    k1 = 5
    multiplier1 = 2
    # Output: [8,4,6,5,6]

    nums2 = [1, 2]
    k2 = 3
    multiplier2 = 4
    # Output: [16,8]

    print(test.getFinalState(nums1, k1, multiplier1))
    print(test.getFinalState(nums2, k2, multiplier2))
