from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # BASIC ---------------------------------------------------------------
        s = [i for i in s]
        for i in range(len(spaces)-1, -1, -1):
            s.insert(spaces[i], ' ')
        return ''.join(s)


if __name__ == "__main__":
    test = Solution()

    s1 = "LeetcodeHelpsMeLearn"
    spaces1 = [8, 13, 15]
    # Output: "Leetcode Helps Me Learn"

    s2 = "icodeinpython"
    spaces2 = [1, 5, 7, 9]
    # Output: "i code in py thon"

    s3 = "spacing"
    spaces3 = [0, 1, 2, 3, 4, 5, 6]
    # Output: " s p a c i n g"

    s4 = "EnjoyYourCoffee"
    spaces4 = [5, 9]
    # Output: "Enjoy Your Coffee"

    print(test.addSpaces(s1, spaces1))
    print(test.addSpaces(s2, spaces2))
    print(test.addSpaces(s3, spaces3))
    print(test.addSpaces(s4, spaces4))
