from typing import List


class Solution:
    def getWords(self, x):
        if x in 'qwertyuiop':
            return 1
        elif x in 'asdfghjkl':
            return 2
        else:
            return 3

    def findWords(self, words: List[str]) -> List[str]:
        result = []
        for i in words:
            m = set(i.lower())
            temp = set(map(self.getWords, m))
            if len(temp) == 1:
                result += [i]
        return result


if __name__ == "__main__":
    test = Solution()

    words1 = ["Hello", "Alaska", "Dad", "Peace"]
    # Output: ["Alaska","Dad"]

    words2 = ["omk"]
    # Output: []

    words3 = ["adsdf", "sfd"]
    # Output: ["adsdf","sfd"]

    print(test.findWords(words1))
    # print(test.findWords(words2))
    # print(test.findWords(words3))
