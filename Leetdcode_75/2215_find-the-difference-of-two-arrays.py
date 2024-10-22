from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        # CARA-1 ==============================================
        # wadah = []
        # for i in nums1:
        #     if i in nums2:
        #         wadah.append(i)

        # for i in wadah:
        #     nums1.remove(i)
        #     nums2.remove(i)

        # return [list(nums1), list(nums2)]

        # CARA-2 ==============================================
        # sama = nums1 & nums2
        # nums1 -= sama
        # nums2 -= sama
        
        # return [list(nums1), list(nums2)]


        # CARA-3 ==============================================
        angka1 = nums1 - nums2
        angka2 = nums2 - nums1

        return [list(angka1), list(angka2)]


if __name__ == "__main__":
    test = Solution()

    a_nums1 = [1, 2, 3]
    a_nums2 = [2, 4, 6]
    # Output: [[1,3],[4,6]]

    b_nums1 = [1, 2, 3, 3]
    b_nums2 = [1, 1, 2, 2]
    # Output: [[3],[]]

    print(test.findDifference(a_nums1, a_nums2))
    print(test.findDifference(b_nums1, b_nums2))
