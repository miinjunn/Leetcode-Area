from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # basic knowledge (still fail)---------------------------------------------
        # n = len(nums)

        # counter = 0
        # posisi_idx = 0
        # sekarang = nums[posisi_idx]
        # temp = 0

        # while True:
        #     if posisi_idx == n-1:
        #         break

        #     temp = max(temp, posisi_idx + sekarang + 1)

        #     if temp >= n-1:
        #         counter += 1
        #         break

        #     sekarang = max(nums[posisi_idx + 1: temp])
        #     asu = nums[posisi_idx + 1:temp]
        #     posisi_idx = (
        #         len(asu) - asu[::-1].index(max(asu)) - 1) + posisi_idx + 1

        #     counter += 1

        #     # print(f'temp: {temp}')
        #     # print(f'sekarang: {sekarang}')
        #     # print(f'posisi_idx: {posisi_idx}')
        #     # print(f'counter: {counter}\n')

        # return counter

        # optimize ---------------------------------------------
        n = len(nums)
        total_jump = 0
        sekarang = 0
        temp = 0
        for i in range(0, n-1):
            temp = max(temp, i+nums[i])
            if i == sekarang:
                total_jump += 1
                sekarang = temp

        return total_jump


if __name__ == "__main__":
    test = Solution()

    nums00 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
    # Output: 2

    nums0 = [3, 2, 1]
    # Output: 1

    nums1 = [2, 3, 1, 1, 4]
    # Output: 2

    nums2 = [2, 3, 0, 1, 4]
    # Output: 2

    nums3 = [2, 3, 1, 1, 4, 2, 3]
    # Output: 3

    nums4 = [2, 3, 2, 2, 1, 3, 0]
    # Output: salah = 5, benar = 4

    print(test.jump(nums00))
    print(test.jump(nums0))
    print(test.jump(nums1))
    print(test.jump(nums2))
    print(test.jump(nums3))
    print(test.jump(nums4))
