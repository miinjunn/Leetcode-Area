from typing import List
from collections import defaultdict


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # OPTIMIZE=====================================
        nums.sort()
        total_operasi = 0
        kiri = 0
        kanan = len(nums) - 1

        # buat 2 pointer,
        # kiri = pointer sebelah kiri
        # kanan = pointer sebelah kanan

        while kiri < kanan:
            total = nums[kiri] + nums[kanan]
            if total == k:
                total_operasi += 1
                kiri += 1
                kanan -= 1
            elif total > k:
                kanan -= 1
            else:
                kiri += 1
        return total_operasi

        # UN-OPTIMIZE=====================================
        # total_operasi = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == k:
        #             total_operasi += 1
        #             nums.pop(j)
        #             break
        # return total_operasi


test = Solution()
nums1 = [1, 2, 3, 4]
k1 = 5
# Output: 2

nums2 = [3, 1, 3, 4, 3]
k2 = 6
# Output: 1

print(test.maxOperations(nums1, k1))
print(test.maxOperations(nums2, k2))
