from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if set(s) == 1:
            return 1
        if s == "":
            return 0
        n = len(s)
        result = 0
        for i in range(n):
            counter = 0
            wadah = ''
            for j in range(i, n):
                if s[j] not in wadah:
                    wadah += s[j]
                    counter += 1
                else:
                    result = max(result, counter)
                    counter = 1
                    break
            result = max(result, counter)
        result = max(result, counter)
        return result


if __name__ == "__main__":
    test = Solution()

    s1 = "bbbbb"
    # Output: 1

    s2 = "abcabcbb"
    # Output: 3

    s3 = "pwwkew"
    # Output: 3

    s4 = "abcdef"
    # Output: 6

    s5 = " "
    # Output: 1

    s6 = "dvdf"
    # Output: 3

    s7 = ""
    # Output: 0

    print(test.lengthOfLongestSubstring(s1))
    print(test.lengthOfLongestSubstring(s2))
    print(test.lengthOfLongestSubstring(s3))
    print(test.lengthOfLongestSubstring(s4))
    print(test.lengthOfLongestSubstring(s5))
    print(test.lengthOfLongestSubstring(s6))
    print(test.lengthOfLongestSubstring(s7))
