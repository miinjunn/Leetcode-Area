from typing import List


class Solution:
    # ------------ ITS FOR CONSECUTIVE ------------
    # def increasingTriplet_consecutive(self, nums: List[int]) -> bool:
    #     nums = [9] + nums + [0]
    #     res = False
    #     for i in range(1, len(nums) - 1):
    #         if nums[i] > nums[i-1] and nums[i] < nums[i+1]:
    #             res = True
    #             break
    #     return res

    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        mini = float('inf')
        med = float('inf')

        for i in nums:
            if i <= mini:
                mini = i
            elif i <= med:
                med = i
            else:
                return True
        return False


# ----------------------------------------
if __name__ == '__main__':
    test = Solution()
    nums1 = [1, 2, 3, 4, 5]
    # Output: true

    nums2 = [5, 4, 3, 2, 1]
    # Output: false

    nums3 = [2, 1, 5, 0, 4, 6]
    # Output: true

    nums4 = [1, 2, 1, 3]
    # Output: true

    nums5 = [1]
    # Output: false

    nums6 = [2, 4, -2, -3]
    # Output: false

    print(test.increasingTriplet(nums1))
    print(test.increasingTriplet(nums2))
    print(test.increasingTriplet(nums3))
    print(test.increasingTriplet(nums4))
    print(test.increasingTriplet(nums5))
    print(test.increasingTriplet(nums6))
