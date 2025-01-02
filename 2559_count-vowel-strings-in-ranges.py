from typing import List


class Solution:
    # BASIC METHOD ---------------
    # def is_vowel(self, state):
    #     vowel = ["a", "i", "u", "e", "o"]
    #     return state[0] in vowel and state[-1] in vowel

    # def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    #     result = []
    #     for i in queries:
    #         counter = 0
    #         for j in range(i[0], i[1]+1):
    #             if self.is_vowel(words[j]) == True:
    #                 counter += 1
    #         result.append(counter)
    #     return result

    # OPTIMIZED METHOD ---------------
    def is_vowel(self, state):
        vowel = ["a", "i", "u", "e", "o"]
        return state[0] in vowel and state[-1] in vowel

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        kamus = [self.is_vowel(i) for i in words]

        prefix_sum = [0] * (len(words)+1)
        for i in range(1, len(words) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + (1 if kamus[i - 1] else 0)
        print(f"prefix: {prefix_sum}")

        result = []
        for i, j in queries:
            count = prefix_sum[j + 1] - prefix_sum[i]
            result.append(count)

        return result


if __name__ == "__main__":
    test = Solution()

    words1 = ["aba", "bcb", "ece", "aa", "e"]
    queries1 = [[0, 2], [1, 4], [1, 1]]
    # Output: [2,3,0]

    words2 = ["a", "e", "i"]
    queries2 = [[0, 2], [0, 1], [2, 2]]
    # Output: [3,2,1]

    print(test.vowelStrings(words1, queries1))
    print(test.vowelStrings(words2, queries2))
