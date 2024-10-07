class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        result = s[::-1]
        return ' '.join(result)


if __name__ == '__main__':
    test = Solution()

    s = "the sky is blue"
    # Output = "blue is sky the"

    s2 = "  hello world  "
    # Output = "world hello"

    s3 = "a good   example"
    # Output = "example good a"

    print(test.reverseWords(s))
    print(test.reverseWords(s2))
    print(test.reverseWords(s3))
