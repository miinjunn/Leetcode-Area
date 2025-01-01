class Solution:
    def maxScore(self, s: str) -> int:
        result = 0

        for i in range(1, len(s)):
            kiri = s[:i].count('0')
            kanan = s[i:].count('1')
            temp = kiri + kanan
            result = max(result, temp)

        return result


if __name__ == "__main__":
    test = Solution()

    s1 = "011101"
    # Output: 5

    s2 = "00111"
    # Output: 5

    s3 = "1111"
    # Output: 3

    s4 = "00"
    # Output: 1

    print(test.maxScore(s1))
    print(test.maxScore(s2))
    print(test.maxScore(s3))
    print(test.maxScore(s4))
