from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        n = [i for i in range(1, 1+n)]
        return list(combinations(n, k))


if __name__ == '__main__':
    test = Solution()
    n1 = 4
    k1 = 2
    # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    n2 = 1
    k2 = 1
    # Output: [[1]]

    print(test.combine(n1, k1))
    print(test.combine(n2, k2))
