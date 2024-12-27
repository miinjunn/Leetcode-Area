from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)-1, 2):
            result += nums[i] * [nums[i+1]]
        return result


if __name__ == "__main__":
    test = Solution()

    nums1 = [1, 2, 3, 4]
    # Output: [2,4,4,4]

    nums2 = [1, 1, 2, 3]
    # Output: [1,3,3]

    print(test.decompressRLElist(nums1))
    print(test.decompressRLElist(nums2))
