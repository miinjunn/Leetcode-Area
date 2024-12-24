class Solution:
    def toLowerCase(self, s: str) -> str:
        if s.islower():
            return s
        else:
            return s.lower()


if __name__ == "__main__":
    test = Solution()

    s1 = "Hello"
    # Output: "hello"

    s2 = "here"
    # Output: "here"

    s3 = "LOVELY"
    # Output: "lovely"

    print(test.toLowerCase(s1))
    print(test.toLowerCase(s2))
    print(test.toLowerCase(s3))
