from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        result = 0
        captured = 0
        temp = forts[0]

        for i in range(1, len(forts)):
            if temp == 0:
                captured = 0
                temp = forts[i]

            elif abs(abs(temp) - abs(forts[i])) == 1:
                captured += 1

            elif (temp + forts[i] == 2) or (temp + forts[i] == -2):
                captured = 0
                temp = forts[i]

            else:
                result = max(result, captured)
                captured = 0
                temp = forts[i]

        return result


if __name__ == "__main__":
    test = Solution()

    forts1 = [1, 0, 0, -1, 0, 0, 0, 0, 1]
    # Output: 4

    forts2 = [0, 0, 1, -1]
    # Output: 0

    forts3 = [1, 0, 0, -1, 0, 0, -1, 0, 0, 1]
    # Output: 2

    forts4 = [1, 0, 1, 1, 0, 0, -1, 1]
    # Output: 2

    forts5 = [-1, 0, -1, 0, 1, 1, 1, -1, -1, -1]
    # Output: 1

    forts6 = [-1, -1, 0, 1, 0, 0, 1, -1, 1, 0]
    # Output: 1

    forts7 = [0, -1, -1, 0, -1]
    # Output: 0

    forts8 = [0, 1, 0, -1, 1, -1, -1, 0, 1, 1, 0]
    # Output: 1

    forts9 = [0, 1, 0, 0, -1]
    # Output: 2

    print(test.captureForts(forts1))
    print(test.captureForts(forts2))
    print(test.captureForts(forts3))
    print(test.captureForts(forts4))
    print(test.captureForts(forts5))
    print(test.captureForts(forts6))
    print(test.captureForts(forts7))
    print(test.captureForts(forts8))
    print(test.captureForts(forts9))
