from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # BASIC -------------------------------
        data = dict()
        for i in strs:
            urut = tuple(sorted(i))

            if urut in data:
                data[urut].append(i)
            else:
                data[urut] = [i]

        return list(data.values())

        # OPTIMIZED -------------------------------
        # data = defaultdict(list)
        # for i in strs:
        #     key = tuple(sorted(i))
        #     data[key].append(i)

        # return list(data.values())


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
