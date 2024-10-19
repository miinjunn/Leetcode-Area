from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        hasil = -1
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                hasil = i
                break
        return hasil


if __name__ == "__main__":
    test = Solution()

    nums1 = [1, 7, 3, 6, 5, 6]
    # Output: 3

    nums2 = [1, 2, 3]
    # Output: -1

    nums3 = [2, 1, -1]
    # Output: 0

    nums4 = [-1,-1,-1,-1,-1,0]
    # Output: 2

    nums5 = [-1,-1,0,0,-1,-1]
    # Output: 2

    print(test.pivotIndex(nums1))
    print(test.pivotIndex(nums2))
    print(test.pivotIndex(nums3))
    print(test.pivotIndex(nums4))
    print(test.pivotIndex(nums5))
