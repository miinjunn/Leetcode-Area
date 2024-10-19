from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # IN-PLACE=====================================
        # gain = [0] + gain
        # for i in range(1, len(gain)):
        #     gain[i] += gain[i-1]
        # return max(gain)

        # TRACKING=====================================
        result = 0
        temp = 0
        for i in gain:
            temp += i
            result = max(result, temp)
        return result


if __name__ == "__main__":
    test = Solution()

    gain1 = [-5, 1, 5, 0, -7]
    # Output: 1

    gain2 = [-4, -3, -2, -1, 4, 3, 2]
    # Output: 0

    print(test.largestAltitude(gain1))
    print(test.largestAltitude(gain2))
