from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.insert(index[i], nums[i])
        
        return result


if __name__ == "__main__":
    test = Solution()

    nums1 = [0, 1, 2, 3, 4]
    index1 = [0, 1, 2, 2, 1]
    # Output: [0,4,1,3,2]

    nums2 = [1, 2, 3, 4, 0]
    index2 = [0, 1, 2, 3, 0]
    # Output: [0,1,2,3,4]

    print(test.createTargetArray(nums1, index1))
    print(test.createTargetArray(nums2, index2))
