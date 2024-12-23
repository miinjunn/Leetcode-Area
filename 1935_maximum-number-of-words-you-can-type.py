class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ...


if __name__ == "__main__":
    test = Solution()

    text1 = "hello world"
    brokenLetters1 = "ad"
    # Output: 1
    # Explanation: We cannot type "world" because the 'd' key is broken.

    text2 = "leet code"
    brokenLetters2 = "lt"
    # Output: 1
    # Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.

    text3 = "leet code"
    brokenLetters3 = "e"
    # Output: 0
    # Explanation: We cannot type either word because the 'e' key is broken.
