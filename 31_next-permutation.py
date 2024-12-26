from itertools import permutations
from typing import List


class Solution:
    # basic method ------------------------------------------------
    def nextPermutation(self, nums: List[int]) -> None:
        n = sorted(nums)
        temp = sorted(set(permutations(n)))
        print(temp)
        if tuple(nums) in temp:
            posisi = temp.index(tuple(nums))
            if posisi == len(temp)-1:
                nums[:] = temp[0]
            else:
                nums[:] = temp[posisi+1]


if __name__ == "__main__":
    test = Solution()

    nums1 = [1, 2, 3]
    # Output: [1,3,2]

    nums2 = [3, 2, 1]
    # Output: [1,2,3]

    nums3 = [1, 1, 5]
    # Output: [1,5,1]

    nums4 = [1, 5, 1]
    # Output: [5,1,1]

    test.nextPermutation(nums1)
    test.nextPermutation(nums2)
    test.nextPermutation(nums3)
    test.nextPermutation(nums4)

    print(nums1)
    print(nums2)
    print(nums3)
    print(nums4)
