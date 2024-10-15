from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        temp = None
        for _ in range(len(nums)):
            print(f'iter: {_}')
            checkpoint = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
                    checkpoint = True
            if checkpoint != True:
                break
        return nums


if __name__ == '__main__':
    test = Solution()
    nums1 = [2, 0, 2, 1, 1, 0]
    # Output: [0,0,1,1,2,2]

    nums2 = [2, 0, 1]
    # Output: [0,1,2]

    print(test.sortColors(nums1))
    print(test.sortColors(nums2))
