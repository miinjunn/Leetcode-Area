from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # BASIC -------------------------------
        # def anagram(x, y):
        #     return sorted(x) == sorted(y)

        # new_strs = [''.join(sorted(i)) for i in strs]
        # data = dict(Counter(new_strs))
        # res = [[] for _ in range(len(data))]

        # # print(f'data: {data}')

        # for i in strs:
        #     for ky, vl in data.items():
        #         if anagram(i, ky):
        #             res[list(data).index(ky)].append(i)

        # return res

        # OPTIMIZED -------------------------------
        data = defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))
            data[key].append(i)

        return list(data.values())


if __name__ == "__main__":
    test = Solution()

    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    strs2 = [""]
    # Output: [[""]]

    strs3 = ["a"]
    # Output: [["a"]]

    strs4 = ["", ""]

    print(test.groupAnagrams(strs1))
    print(test.groupAnagrams(strs2))
    print(test.groupAnagrams(strs3))
    print(test.groupAnagrams(strs4))
