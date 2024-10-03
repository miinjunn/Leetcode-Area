from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = True
        if len(s) != len(t):
            return False
        for i in s:
            if s.count(i) != t.count(i):
                res = False
                break
        return res

    def isAnagram_v2(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        # print(s, t)
        if s == t:
            return True
        else:
            return False

    def isAnagram_v3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    test = Solution()
    s1 = "anagram"
    t1 = "nagaram"
    # Output: true
    s2 = "rat"
    t2 = "car"
    # Output: false

    s3 = "a"
    t3 = "ab"
    # Output: false

    s4 = "hello"
    t4 = "helo"
    # Output: false

    print(test.isAnagram(s1, t1))
    print(test.isAnagram(s2, t2))
    print(test.isAnagram(s3, t3))
    print(test.isAnagram(s4, t4))
    print('')
    print(test.isAnagram_v2(s1, t1))
    print(test.isAnagram_v2(s2, t2))
    print(test.isAnagram_v2(s3, t3))
    print(test.isAnagram_v2(s4, t4))
    print('')
    print(test.isAnagram_v3(s1, t1))
    print(test.isAnagram_v3(s2, t2))
    print(test.isAnagram_v3(s3, t3))
    print(test.isAnagram_v3(s4, t4))
