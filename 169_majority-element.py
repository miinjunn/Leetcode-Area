from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # BASIC METHOD -------------------
        # me = len(nums) // 2
        # for i in set(nums):
        #     if nums.count(i) > me:
        #         return i

        # LIST COMPREHENSION METHOD -------------------
        me = len(nums) // 2
        result = [i for i in set(nums) if nums.count(i) > me]
        return result[0]


if __name__ == "__main__":
    test = Solution()

    nums1 = [3, 2, 3]
    # Output: 3

    nums2 = [2, 2, 1, 1, 1, 2, 2]
    # Output: 2

    print(test.majorityElement(nums1))
    print(test.majorityElement(nums2))
