from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        genap = 0
        ganjil = 1
        n = len(nums)
        result = [0] * n
        while genap <= n-2 and ganjil <= n-1:
            for i in nums:
                if i % 2:
                    result[ganjil] = i
                    ganjil += 2
                else:
                    result[genap] = i
                    genap += 2
        return result


if __name__ == "__main__":
    test = Solution()

    nums1 = [4, 2, 5, 7]
    # Output: [4,5,2,7]
    # Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

    nums2 = [2, 3]
    # Output: [2,3]

    nums3 = [1,8]
    # Output: [8,1]

    print(test.sortArrayByParityII(nums1))
    print(test.sortArrayByParityII(nums2))
    print(test.sortArrayByParityII(nums3))
