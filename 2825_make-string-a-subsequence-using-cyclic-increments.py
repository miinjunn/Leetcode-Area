class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        j = 0

        while j < len(str2):
            if i >= len(str1):
                return False

            if (str1[i] == str2[j]) or (chr(ord(str1[i])+1) == str2[j]):
                i += 1
                j += 1
            elif (str1[i] == 'z' and str2[j] == 'a'):
                i += 1
                j += 1
            else:
                i += 1

        return True


if __name__ == "__main__":
    test = Solution()

    str1_1 = "abc"
    str2_1 = "ad"
    # Output: true

    str1_2 = "zc"
    str2_2 = "ad"
    # Output: true

    str1_3 = "ab"
    str2_3 = "d"
    # Output: false

    str1_4 = "eao"
    str2_4 = "ofa"
    # Output: false

    str1_5 = "f"
    str2_5 = "f"
    # Output: true

    str1_6 = "ff"
    str2_6 = "fg"
    # Output: true

    print(test.canMakeSubsequence(str1_1, str2_1))
    print(test.canMakeSubsequence(str1_2, str2_2))
    print(test.canMakeSubsequence(str1_3, str2_3))
    print(test.canMakeSubsequence(str1_4, str2_4))
    print(test.canMakeSubsequence(str1_5, str2_5))
    print(test.canMakeSubsequence(str1_6, str2_6))
