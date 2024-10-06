class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = 'aiueoAIUEO'
        s_vowel = [i for i in s if i in vowel][::-1]
        result = ''
        counter = 0
        for i in range(len(s)):
            if s[i] in vowel:
                result += s_vowel[counter]
                counter += 1
            else:
                result += s[i]
        return result


if __name__ == '__main__':
    test = Solution()
    s = "IceCreAm"
    # Output = "AceCreIm"

    s2 = "leetcode"
    # Output = "leotcede"

    print(test.reverseVowels(s))
    print(test.reverseVowels(s2))
