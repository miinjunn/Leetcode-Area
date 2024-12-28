from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = sorted(set(arr))
        result = []
        for i in arr:
            result.append(rank.index(i)+1)
        return result


if __name__ == "__main__":
    test = Solution()

    arr1 = [40, 10, 20, 30]
    # Output: [4,1,2,3]

    arr2 = [100, 100, 100]
    # Output: [1,1,1]

    arr3 = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    # Output: [5,3,4,2,8,6,7,1,3]

    arr4 = [40, 10, 20, 10, 30]
    # Output: [4,1,2,1,3]

    print(test.arrayRankTransform(arr1))
    print(test.arrayRankTransform(arr2))
    print(test.arrayRankTransform(arr3))
    print(test.arrayRankTransform(arr4))
