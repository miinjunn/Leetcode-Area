from typing import List
from collections import deque


class Solution:
    # basic solution --> O(n^2)
    # def continuousSubarrays(self, nums: List[int]) -> int:
    #     result = 0
    #     counter = 0
    #     result_list = []
    #     n = len(nums)
    #     while counter < n:
    #         for i in range(n-counter):
    #             temp = nums[i:i+counter+1]
    #             maks = max(temp)
    #             mins = min(temp)
    #             if abs(maks - mins) >= 0 and abs(maks - mins) <= 2:
    #                 result_list.append(temp)
    #                 result += 1
    #         counter += 1
    #     return result

    # optimize solution --> O(n)
    def continuousSubarrays(self, nums: List[int]) -> int:
        result = 0
        left = 0
        max_deque = deque()
        min_deque = deque()

        for right in range(len(nums)):
            # Maintain max deque
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # Maintain min deque
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # Check if Condition Valid
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Count Valid Condition
            result += right - left + 1
        return result


if __name__ == "__main__":
    test = Solution()

    nums1 = [5, 4, 2, 4]
    # Output: 8

    nums2 = [1, 2, 3]
    # Output: 6

    nums3 = [1, 10]
    # Output: 2

    nums4 = [31, 30, 31, 32]
    # Output: 10

    nums5 = [54, 53, 53, 52, 53, 54, 53, 52]
    # Output:

    nums6 = [1, 42, 41, 42, 41, 41, 40, 39, 38]
    # Output:

    nums7 = [60, 65, 66, 67, 66, 66, 65, 64, 65, 65, 64]
    # Output:

    print(test.continuousSubarrays(nums1))
    print(test.continuousSubarrays(nums2))
    print(test.continuousSubarrays(nums3))
    print(test.continuousSubarrays(nums4))
    print(test.continuousSubarrays(nums5))
    print(test.continuousSubarrays(nums6))
    print(test.continuousSubarrays(nums7))
