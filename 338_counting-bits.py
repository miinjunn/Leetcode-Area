from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            temp = bin(i)[2:]
            result.append(temp.count('1'))

        return result


if __name__ == "__main__":
    test = Solution()

    n1 = 2
    # Output: [0,1,1]

    n2 = 5
    # Output: [0,1,1,2,1,2]

    print(test.countBits(n1))
    print(test.countBits(n2))