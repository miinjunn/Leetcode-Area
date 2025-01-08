from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = sorted(heights)
        counter = 0
        for i in range(len(heights)):
            if heights[i] != temp[i]:
                counter += 1

        return counter


if __name__ == "__main__":
    test = Solution()

    heights1 = [1, 1, 4, 2, 1, 3]
    # Output: 3

    heights2 = [5, 1, 2, 3, 4]
    # Output: 5

    heights3 = [1, 2, 3, 4, 5]
    # Output: 0

    print(test.heightChecker(heights1))
    print(test.heightChecker(heights2))
    print(test.heightChecker(heights3))
