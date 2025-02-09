from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # result = nums[0]
        # for i in range(len(nums) - 1):
        #     temp = nums[i]
        #     for j in range(i+1, len(nums)):
        #         temp *= nums[j]
        #         result = max(temp, result, nums[j])

        # return result

        # OPTMIZED METHOD
        if not nums:
            return 0

        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]
            if current < 0:
                max_product, min_product = min_product, max_product

            max_product = max(current, max_product * current)
            min_product = min(current, min_product * current)

            result = max(result, max_product)

        return result


if __name__ == "__main__":
    test = Solution()

    nums = [2, 3, -2, 4]
    # Output: 6

    nums2 = [-2, 0, -1]
    # Output: 0

    print(test.maxProduct(nums))
    print(test.maxProduct(nums2))
