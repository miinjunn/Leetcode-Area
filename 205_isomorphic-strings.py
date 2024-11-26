class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if len(set(s)) != len(set(t)):
        #     return False
        if len(set(t)) < len(set(s)):
            s, t = t, s
            
        result = {}
        for i in range(len(s)):
            if s[i] not in result:
                result[s[i]] = t[i]
            elif result[s[i]] != t[i]:
                return False

        return True


if __name__ == "__main__":
    test = Solution()

    s1 = "egg"
    t1 = "add"
    # Output: true

    s2 = "foo"
    t2 = "bar"
    # Output: false

    s3 = "paper"
    t3 = "title"
    # Output: true

    s4 = "bbbaaaba"
    t4 = "aaabbbba"
    # Output: false

    s5 = "badc"
    t5 = "baba"
    # Output: false

    print(test.isIsomorphic(s1, t1))
    print(test.isIsomorphic(s2, t2))
    print(test.isIsomorphic(s3, t3))
    print(test.isIsomorphic(s4, t4))
    print(test.isIsomorphic(s5, t5))
