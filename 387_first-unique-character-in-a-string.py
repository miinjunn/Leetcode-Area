class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp = ""
        for i in s:
            if i not in temp:
                temp += i

        for i in temp:
            if s.count(i) == 1:
                return s.index(i)

        return -1


if __name__ == "__main__":
    test = Solution()

    s1 = "leetcode"
    # Output: 0

    s2 = "loveleetcode"
    # Output: 2

    s3 = "aabb"
    # Output: -1

    print(test.firstUniqChar(s1))
    print(test.firstUniqChar(s2))
    print(test.firstUniqChar(s3))
