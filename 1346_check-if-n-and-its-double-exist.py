from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        m = len(arr)
        for i in range(m):
            for j in range(m):
                if i == j:
                    continue
                if arr[j] * 2 == arr[i]:
                    print(f"i: {i, arr[i]}")
                    print(f"j: {j, arr[j]}")
                    return True
        return False


if __name__ == "__main__":
    test = Solution()

    arr1 = [10, 2, 5, 3]
    # Output: true

    arr2 = [3, 1, 7, 11]
    # Output: false

    arr3 = [0, 0]
    # Output: true

    arr4 = [-2, 0, 10, -19, 4, 6, -8]
    # Output: false

    arr5 = [2, 3, 3, 0, 0]
    # Output: true

    print(test.checkIfExist(arr1))
    print(test.checkIfExist(arr2))
    print(test.checkIfExist(arr3))
    print(test.checkIfExist(arr4))
    print(test.checkIfExist(arr5))
