from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(set(nums)) == 1:
            return True

        n = len(nums)
        posisi = 0
        sekarang = nums[posisi]
        temp = 0
        while True:
            if sekarang == 0:
                return False

            temp = max(temp, posisi + nums[posisi] + 1)
            if temp >= n:
                return True

            sekarang = max(nums[posisi+1:temp])
            posisi = posisi + 1 + nums[posisi+1:temp].index(sekarang)
            # print(f'sekarang: {sekarang}')
            # print(f'posisi: {posisi}')


if __name__ == "__main__":
    test = Solution()

    nums00 = [4, 4, 4, 0, 3, 1, 2, 1, 1, 3, 4]
    # Output: true

    nums0 = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
    # Output: true

    nums1 = [2, 3, 1, 1, 4]
    # Output: true

    nums2 = [3, 2, 1, 0, 4]
    # Output: false

    nums3 = [0]
    # Output: true

    nums4 = [0, 1]
    # Output: False

    nums5 = [2, 0]
    # Output: True

    nums6 = [1, 1, 0, 1]
    # Output: False

    print(test.canJump(nums00))
    print(test.canJump(nums0))
    print(test.canJump(nums1))
    print(test.canJump(nums2))
    print(test.canJump(nums3))
    print(test.canJump(nums4))
    print(test.canJump(nums5))
    print(test.canJump(nums6))
