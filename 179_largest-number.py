from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if set(nums) == {0}:
            return '0'

        nums_str = [str(i) for i in nums]
        nums_str = sorted(nums_str, key=lambda i: i*10, reverse=True)
        print(f'nums: {nums_str}')
        return "".join(nums_str)


if __name__ == "__main__":
    test = Solution()

    nums1 = [10, 2]
    # Output: "210"

    nums2 = [3, 30, 34, 5, 9]
    # Output: "9534330"

    nums3 = [0, 0, 0]
    # Output: "0"

    print(test.largestNumber(nums1))
    print(test.largestNumber(nums2))
    print(test.largestNumber(nums3))
