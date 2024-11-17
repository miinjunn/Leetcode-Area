from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = [nums[nums[i]] for i in range(len(nums))]
        return result


if __name__ == "__main__":
    test = Solution()

    nums1 = [0, 2, 1, 5, 3, 4]
    # Output: [0,1,2,4,5,3]

    nums2 = [5, 0, 1, 2, 3, 4]
    # Output: [4,5,0,1,2,3]

    print(test.buildArray(nums1))
    print(test.buildArray(nums2))
