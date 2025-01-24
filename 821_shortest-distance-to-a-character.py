from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = []
        kamus = [i for i in range(len(s)) if s[i] == c]

        for i in range(len(s)):
            inner_temp = []
            for j in range(len(kamus)):
                inner_temp.append(abs(i-kamus[j]))
            result.append(min(inner_temp))

        return result


if __name__ == "__main__":
    test = Solution()

    s1 = "loveleetcode"
    c1 = "e"
    # Output: [3,2,1,0,1,0,0,1,2,2,1,0]

    s2 = "aaab"
    c2 = "b"
    # Output: [3,2,1,0]

    print(test.shortestToChar(s1, c1))
    print(test.shortestToChar(s2, c2))
