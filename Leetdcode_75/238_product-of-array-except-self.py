from typing import List
import math
import functools
import operator


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ----------------------------------------------------------------
        # CODE VERSION 1.0 [base]
        # result = []
        # counter = 0
        # for i in range(len(nums)):
        #     temp = nums.copy()
        #     temp.pop(i)

        #     if 0 in temp:
        #         result.append(0)
        #     else:
        #         product = 1
        #         for j in temp:
        #             product *= j

        #         result.append(product)
        #         counter += 1
        # return result

        # ----------------------------------------------------------------
        # CODE VERSION 2.0 [fast]
        result = [0] * len(nums)
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]
            if 0 in temp:
                result[i] = 0
            else:
                # result[i] = eval('*'.join(map(str, temp)))  # cara-1
                result[i] = math.prod(temp)  # cara-2
                # result[i] = functools.reduce(operator.mul, temp, 1)  # cara-3

        return result

        # ----------------------------------------------------------------
        # CODE VERSION 3.0 [optimize]
        # n = len(nums)
        # result = [1] * n

        # # Calculate the product of all numbers to the left of each index
        # left_product = 1
        # for i in range(n):
        #     result[i] *= left_product
        #     left_product *= nums[i]
        # print(f'left: {result}')

        # # Calculate the product of all numbers to the right of each index
        # right_product = 1
        # for i in range(n-1, -1, -1):
        #     result[i] *= right_product
        #     right_product *= nums[i]
        # return result


if __name__ == '__main__':
    test = Solution()
    nums1 = [1, 2, 3, 4]
    # Output: [24,12,8,6]

    nums2 = [-1, 1, 0, -3, 3]
    # Output: [0,0,9,0,0]

    print(test.productExceptSelf(nums1))
    print(test.productExceptSelf(nums2))
