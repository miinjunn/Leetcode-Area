from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        n = len(timeSeries)
        for i in range(n - 1):
            if timeSeries[i] + duration - 1 < timeSeries[i+1]:
                result += duration
            else:
                result += timeSeries[i+1] - timeSeries[i]
        return result + duration


if __name__ == "__main__":
    test = Solution()

    timeSeries1 = [1, 4]
    duration1 = 2
    # Output: 4

    timeSeries2 = [1, 2]
    duration2 = 2
    # Output: 3

    print(test.findPoisonedDuration(timeSeries1, duration1))
    print(test.findPoisonedDuration(timeSeries2, duration2))
