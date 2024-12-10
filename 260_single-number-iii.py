from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # solusi basic -----------------------------------------------------
        # n = set(nums)
        # result = []
        # for i in n:
        #     if nums.count(i) <= 1:
        #         result.append(i)
        # return result

        # solusi dengan counter --------------------------------------------
        kamus = Counter(nums)
        result = [ky for ky, vl in kamus.items() if vl == 1]
        return result


if __name__ == "__main__":
    test = Solution()

    nums1 = [1, 2, 1, 3, 2, 5]
    # Output: [3,5]

    nums2 = [-1, 0]
    # Output: [-1,0]

    nums3 = [0, 1]
    # Output: [1,0]

    print(test.singleNumber(nums1))
    print(test.singleNumber(nums2))
    print(test.singleNumber(nums3))
