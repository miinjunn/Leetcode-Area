from typing import List
# from itertools import combinations


class Solution:
    # basic method ------------------------
    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     temp = combinations(sorted(nums), 4)
    #     result = []
    #     for i in temp:
    #         if i not in result and sum(i) == target:
    #             result.append(i)
    #     return result

    # optimize (two pointer) method ------------------------
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum < target:
                        left += 1
                    elif current_sum > target:
                        right -= 1
                    else:
                        result.append(
                            [nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicate for 3rd number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        # Skip duplicate for 4th number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

        return result


if __name__ == "__main__":
    test = Solution()

    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    # Output: [[2,2,2,2]]

    nums3 = [-5, 5, 4, -3, 0, 0, 4, -2]
    target3 = 4
    # Output: [[-5,0,4,5],[-3,-2,4,5]]

    print(test.fourSum(nums1, target1))
    print(test.fourSum(nums2, target2))
    print(test.fourSum(nums3, target3))
