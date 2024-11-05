from typing import List
from collections import Counter


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # CARA-1 (change in-place, return same list)
        m = nums.count(val)
        for _ in range(m):
            nums.remove(val)
        return len(nums)

        # CARA-2 (return new list)
        # arx = [i for i in nums if i != val]
        # return len(arx)

        # CARA-3, mirip dengan cara-2 (return new list)
        # arx = [vl for ky, vl in enumerate(nums) if vl != val]
        # return len(arx)


if __name__ == "__main__":
    test = Solution()

    nums1 = [3, 2, 2, 3]
    val1 = 3
    # Output: 2, nums = [2,2,_,_]

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    # Output: 5, nums = [0,1,4,0,3,_,_,_]

    print(test.removeElement(nums1, val1))
    print(test.removeElement(nums2, val2))
