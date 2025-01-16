from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for i in nums1:
            temp = nums2[nums2.index(i):]
            inner_res = 0

            for j in temp:
                if j > i:
                    inner_res = j
                    break
                else:
                    inner_res = -1

            result.append(inner_res)
        return result


if __name__ == "__main__":
    test = Solution()

    a_nums1 = [4, 1, 2]
    a_nums2 = [1, 3, 4, 2]
    # Output: [-1,3,-1]

    b_nums1 = [2, 4]
    b_nums2 = [1, 2, 3, 4]
    # Output: [3,-1]

    print(test.nextGreaterElement(a_nums1, a_nums2))
    print(test.nextGreaterElement(b_nums1, b_nums2))
