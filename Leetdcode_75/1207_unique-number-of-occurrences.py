from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        temp = set(arr)
        wadah = []

        for i in temp:
            if arr.count(i) not in wadah:
                wadah.append(arr.count(i))
            else:
                return False
        return True


if __name__ == "__main__":
    test = Solution()
    arr1 = [1, 2, 2, 1, 1, 3]
    # Output: true

    arr2 = [1, 2]
    # Output: false

    arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    # Output: true

    print(test.uniqueOccurrences(arr1))
    print(test.uniqueOccurrences(arr2))
    print(test.uniqueOccurrences(arr3))
