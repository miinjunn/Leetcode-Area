from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = sorted(arr, key=lambda x: [bin(x).count("1"), x])
        return res


if __name__ == "__main__":
    test = Solution()

    arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # Output: [0,1,2,4,8,3,5,6,7]

    # Explantion: [0] is the only integer with 0 bits.
    # [1,2,4,8] all have 1 bit.
    # [3,5,6] have 2 bits.
    # [7] has 3 bits.
    # The sorted array by bits is [0,1,2,4,8,3,5,6,7]

    arr2 = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    # Output: [1,2,4,8,16,32,64,128,256,512,1024]

    arr3 = [10000, 10000]
    # Output: [10000,10000]

    print(test.sortByBits(arr1))
    print(test.sortByBits(arr2))
    print(test.sortByBits(arr3))
