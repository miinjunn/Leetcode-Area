class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(s) != len(pattern):
            return False

        if len(set(s)) < len(set(pattern)):
            pattern, s = s, pattern

        result = {}
        for i in range(len(pattern)):
            if pattern[i] not in result:
                result[pattern[i]] = s[i]

            elif result[pattern[i]] != s[i]:
                return False
        return True


if __name__ == "__main__":
    test = Solution()

    pattern1 = "abba"
    s1 = "dog cat cat dog"
    # Output: true

    pattern2 = "abba"
    s2 = "dog cat cat fish"
    # Output: false

    pattern3 = "aaaa"
    s3 = "dog cat cat dog"
    # Output: false

    pattern4 = "aba"
    s4 = "cat cat cat dog"
    # Output: false

    print(test.wordPattern(pattern1, s1))
    print(test.wordPattern(pattern2, s2))
    print(test.wordPattern(pattern3, s3))
    print(test.wordPattern(pattern4, s4))


s1 = "dog cat cat dog"
s1 = s1.split()
