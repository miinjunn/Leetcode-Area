from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(0, len(nums)-k+1):
            temp = nums[i:i+k]

            cons = True
            for j in range(1, len(temp)):
                if temp[j] - temp[j-1] != 1:
                    cons = False
                    break

            if temp != sorted(temp):
                result += [-1]
            elif cons == False:
                result += [-1]
            else:
                result += [max(temp)]

        return result


if __name__ == "__main__":
    test = Solution()

    nums1 = [1, 2, 3, 4, 3, 2, 5]
    k1 = 3
    # Output: [3,4,-1,-1,-1]

    nums2 = [2, 2, 2, 2, 2]
    k2 = 4
    # Output: [-1,-1]

    nums3 = [3, 2, 3, 2, 3, 2]
    k3 = 2
    # Output: [-1,3,-1,3,-1]

    print(test.resultsArray(nums1, k1))
    print(test.resultsArray(nums2, k2))
    print(test.resultsArray(nums3, k3))
