from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # # LAZY OPTION ----------------------------------------------
        # total = nums.count(0)
        # while 0 in nums:
        #     nums.remove(0)
        # temp = nums + ([0]*total)
        # nums[:] = temp
        # print(nums)

        # OPTIMIZE ----------------------------------------------
        last_non_zero = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1
        print(f'nums before fill with 0: {nums}')

        for i in range(last_non_zero, n):
            nums[i] = 0
        print(f'nums after fill with 0: {nums}')


if __name__ == '__main__':
    test = Solution()

    nums1 = [0, 1, 0, 3, 12]
    # Output: [1,3,12,0,0]

    nums2 = [0]
    # Output: [0]

    test.moveZeroes(nums1)
    test.moveZeroes(nums2)
