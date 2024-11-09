from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        kiri = 0
        kanan = len(s)-1
        tengah = len(s) // 2

        while kiri < tengah:
            s[kiri], s[kanan] = s[kanan], s[kiri]
            kiri += 1
            kanan -= 1
        return s


if __name__ == "__main__":
    test = Solution()
    s1 = ["h", "e", "l", "l", "o"]
    # Output: ["o","l","l","e","h"]

    s2 = ["H", "a", "n", "n", "a", "h"]
    # Output: ["h","a","n","n","a","H"]

    print(test.reverseString(s1))
    print(test.reverseString(s2))
