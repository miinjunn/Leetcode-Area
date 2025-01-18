from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp = {i for i in range(1, len(nums)+1)}
        # print(f"temp: {temp}")
        n = set(nums)
        return list(temp - n)


if __name__ == "__main__":
    test = Solution()

    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    # Output: [5,6]

    nums2 = [1, 1]
    # Output: [2]

    print(test.findDisappearedNumbers(nums1))
    print(test.findDisappearedNumbers(nums2))
