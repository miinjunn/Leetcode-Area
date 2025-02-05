# from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False
        
        counter = 0
        cek = 0

        for i in range(len(s1)):
            if counter > 2 or cek > 0:
                return False

            if s1[i] != s2[i]:
                counter += 1
            if s1[i] not in s2:
                cek += 1

            if s2[i] not in s1:
                cek += 1

        return counter % 2 == 0


if __name__ == "__main__":
    test = Solution()

    s1_1 = "bank"
    s2_1 = "kanb"
    # Output: true

    s1_2 = "attack"
    s2_2 = "defend"
    # Output: false

    s1_3 = "kelb"
    s2_3 = "kelb"
    # Output: true

    s1_4 = "aa"
    s2_4 = "ac"
    # Output: true

    s1_5 = "caa"
    s2_5 = "aaz"
    # Output: true

    print(test.areAlmostEqual(s1_1, s2_1))
    print(test.areAlmostEqual(s1_2, s2_2))
    print(test.areAlmostEqual(s1_3, s2_3))
    print(test.areAlmostEqual(s1_4, s2_4))
    print(test.areAlmostEqual(s1_5, s2_5))
