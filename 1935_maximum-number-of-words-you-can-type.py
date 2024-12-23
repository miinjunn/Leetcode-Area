class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        broken = [i for i in brokenLetters]

        for i in broken:
            for j in range(len(words)):
                if i in words[j]:
                    words[j] = ''

        counter = [1 for i in words if i != '']
        return len(counter)


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

    text4 = "abc de"
    brokenLetters4 = ""

    print(test.canBeTypedWords(text1, brokenLetters1))
    print(test.canBeTypedWords(text2, brokenLetters2))
    print(test.canBeTypedWords(text3, brokenLetters3))
    print(test.canBeTypedWords(text4, brokenLetters4))
