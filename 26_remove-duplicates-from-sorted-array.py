from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = set(nums)
        nums.sort()
        print(nums)
        return len(nums)


if __name__ == "__main__":
    test = Solution()

    nums1 = [1, 1, 2]
    # Output: 2, nums = [1,2,_]

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

    nums3 = [-1, 0, 0, 0, 0, 3, 3]
    # Output: 3, nums = [-1,0,3]

    # print(test.removeDuplicates(nums1))
    # print(test.removeDuplicates(nums2))
    print(test.removeDuplicates(nums3))
