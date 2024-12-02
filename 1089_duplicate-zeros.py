
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # in-place array modification
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] != 0:
                i += 1
            else:
                arr.insert(i, 0)
                arr.pop()
                i += 2

        # solusi create new array, then replace old arr with new arr
        # result = []
        # for i in arr:
        #     if i == 0:
        #         result.append(i)
        #     result.append(i)
        # arr[:] = result[:len(arr)]

        
if __name__ == "__main__":
    test = Solution()

    arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
    # Output: [1,0,0,2,3,0,0,4]

    arr2 = [1, 2, 3]
    # Output: [1,2,3]

    test.duplicateZeros(arr1)
    test.duplicateZeros(arr2)
    print(arr1)
    print(arr2)
