class Solution:
    def reverseWords(self, s: str) -> str:
        kalimat = s.split()
        for i in range(len(kalimat)):
            kalimat[i] = kalimat[i][::-1]
        
        return " ".join(kalimat)


if __name__ == "__main__":
    test = Solution()

    s1 = "Let's take LeetCode contest"
    # Output: "s'teL ekat edoCteeL tsetnoc"

    s2 = "Mr Ding"
    # Output: "rM gniD"

    print(test.reverseWords(s1))
    print(test.reverseWords(s2))
