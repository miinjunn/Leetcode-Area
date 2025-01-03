from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        tidak_ada = []
        result = []
        kamus = Counter(arr1)

        for i in arr2:
            if i in kamus:
                result += [i] * kamus[i]

        for i in set(arr1):
            if i not in arr2:
                tidak_ada += [i] * kamus[i]

        tidak_ada.sort()

        return result + tidak_ada


if __name__ == "__main__":
    test = Solution()

    arr1_a = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2_a = [2, 1, 4, 3, 9, 6]
    # Output: [2,2,2,1,4,3,3,9,6,7,19]

    arr1_b = [28, 6, 22, 8, 44, 17]
    arr2_b = [22, 28, 8, 6]
    # Output: [22,28,8,6,17,44]

    print(test.relativeSortArray(arr1_a, arr2_a))
    print(test.relativeSortArray(arr1_b, arr2_b))
