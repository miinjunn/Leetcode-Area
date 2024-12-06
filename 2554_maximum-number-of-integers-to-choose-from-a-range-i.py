from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = set(banned)
        result = 0
        isi = 0
        for i in range(1, min(n, maxSum)+1):
            if i in ban:
                continue

            if isi + i > maxSum:
                break

            isi += i
            result += 1

        return result


if __name__ == "__main__":
    test = Solution()

    banned1 = [1, 6, 5]
    n1 = 5
    maxSum1 = 6
    # Output: 2

    banned2 = [1, 2, 3, 4, 5, 6, 7]
    n2 = 8
    maxSum2 = 1
    # Output: 0

    banned3 = [11]
    n3 = 7
    maxSum3 = 50
    # Output: 7

    banned4 = [176, 36, 104, 125, 188, 152, 101, 47, 51, 65, 39, 174, 29, 55, 13, 138, 79, 81, 175, 178, 42, 108, 24, 80, 183, 190, 123, 20, 139, 22, 140, 62, 58, 137, 68, 148, 172, 76, 173, 189, 151, 186, 153, 57, 142, 105,
               133, 114, 165, 118, 56, 59, 124, 82, 49, 94, 8, 146, 109, 14, 85, 44, 60, 181, 95, 23, 150, 97, 28, 182, 157, 46, 160, 155, 12, 67, 135, 117, 2, 25, 74, 91, 71, 98, 127, 120, 130, 107, 168, 18, 69, 110, 61, 147, 145, 38]
    n4 = 3016
    maxSum4 = 240

    print(test.maxCount(banned1, n1, maxSum1))
    print(test.maxCount(banned2, n2, maxSum2))
    print(test.maxCount(banned3, n3, maxSum3))
    print(test.maxCount(banned4, n4, maxSum4))
