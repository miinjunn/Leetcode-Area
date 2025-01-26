from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        # CARA-1 --------------------------------------------
        # c = 0
        # for i in r:
        #     if i in m:
        #         if r[i] <= m[i]:
        #             c = 1
        #         else:
        #             c = 0
        #             break
        #     else:
        #         c = 0
        #         break
        # return True if c == 1 else False

        # CARA-2 --------------------------------------------
        c = 0
        for i in r:
            if i not in m:
                return False

            elif r[i] > m[i]:
                return False

            else:
                c = 1

        return True if c == 1 else False


if __name__ == "__main__":
    test = Solution()

    ransomNote1 = "a"
    magazine1 = "b"
    # Output: false

    ransomNote2 = "aa"
    magazine2 = "ab"
    # Output: false

    ransomNote3 = "aa"
    magazine3 = "aab"
    # Output: true

    ransomNote4 = "fihjjjjei"
    magazine4 = "hjibagacbhadfaefdjaeaebgi"
    # Output: false

    ransomNote5 = "ihgg"
    magazine5 = "ch"
    # Output: false

    print(test.canConstruct(ransomNote1, magazine1))
    print(test.canConstruct(ransomNote2, magazine2))
    print(test.canConstruct(ransomNote3, magazine3))
    print(test.canConstruct(ransomNote4, magazine4))
    print(test.canConstruct(ransomNote5, magazine5))
