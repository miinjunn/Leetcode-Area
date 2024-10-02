class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2+str1:
            return ""
        else:
            s1 = len(str1)
            s2 = len(str2)
            result = self.gcd(s1, s2)
            return str1[:result]

    def gcd(self, a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            return self.gcd(a-b, b)
        return self.gcd(a, b-a)


if __name__ == '__main__':
    test = Solution()
    str1 = "ABCABC"
    str2 = "ABC"
    # Output = "ABC"

    str3 = "ABABAB"
    str4 = "ABAB"
    # Output = "AB"

    str5 = "LEET"
    str6 = "CODE"
    # Output = ""

    str7 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
    str8 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    # Output = "TAUXX"

    print(test.gcdOfStrings(str1, str2))
    print(test.gcdOfStrings(str3, str4))
    print(test.gcdOfStrings(str5, str6))
    print(test.gcdOfStrings(str7, str8))
