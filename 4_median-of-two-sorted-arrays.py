from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = sorted(nums1 + nums2)
        n = len(result)
        med = n // 2
        if n % 2:
            return result[med]
        else:
            return (result[med] + result[med-1]) / 2


if __name__ == "__main__":
    test = Solution()

    nums1_a = [1, 3]
    nums2_a = [2]
    # Output: 2.00000

    nums1_b = [1, 2]
    nums2_b = [3, 4]
    # Output: 2.50000

    print(test.findMedianSortedArrays(nums1_a, nums2_a))
    print(test.findMedianSortedArrays(nums1_b, nums2_b))
