from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result_a = 0
        result_b = 0
        trans = [[grid[j][i] for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i] == trans[j]:
                    result_a += 1

                if trans[i] == grid[j]:
                    result_b += 1

        return max(result_a, result_b)


if __name__ == "__main__":
    test = Solution()

    grid1 = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    # Output: 1

    grid2 = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    # Output: 3

    grid3 = [[3, 1, 2, 2], [1, 4, 4, 4], [2, 4, 2, 2], [2, 5, 2, 2]]
    # Output: 3

    grid4 = [[13, 13], [13, 13]]
    # Output: 4

    print(test.equalPairs(grid1))
    print(test.equalPairs(grid2))
    print(test.equalPairs(grid3))
    print(test.equalPairs(grid4))
