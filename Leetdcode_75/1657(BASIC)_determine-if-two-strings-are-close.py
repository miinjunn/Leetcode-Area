class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        wadah1 = {}
        wadah2 = {}
        for i in word1:
            wadah1.update({i: word1.count(i)})

        for x in word2:
            wadah2.update({x: word2.count(x)})

        valu_words1 = list(wadah1.values())
        valu_words2 = list(wadah2.values())

        valu_words1.sort()
        valu_words2.sort()

        print(valu_words1)
        print(valu_words2)

        kk = set(wadah1.keys()) == set(wadah2.keys())
        vv = valu_words1 == valu_words2
        return kk & vv


if __name__ == "__main__":
    test = Solution()

    a_word1 = "abc"
    a_word2 = "bca"
    # Output: true

    b_word1 = "a"
    b_word2 = "aa"
    # Output: false

    c_word1 = "cabbba"
    c_word2 = "abbccc"
    # Output: true

    d_word1 = "abbbzcf"
    d_word2 = "babzzcz"
    # Output: false

    e_word1 = "uau"
    e_word2 = "ssx"
    # Output: false

    f_word1 = "aaabbbbccddeeeeefffff"
    f_word2 = "aaaaabbcccdddeeeeffff"
    # Output: false

    print(test.closeStrings(a_word1, a_word2))
    print(test.closeStrings(b_word1, b_word2))
    print(test.closeStrings(c_word1, c_word2))
    print(test.closeStrings(d_word1, d_word2))
    print(test.closeStrings(e_word1, e_word2))
    print(test.closeStrings(f_word1, f_word2))
