from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # CARA-1:
        # result = min(nums, key=nums.count)
        # return result

        # ---------------------------------------------

        # CARA-2:
        for i in nums:
            if nums.count(i) < 2:
                return i
