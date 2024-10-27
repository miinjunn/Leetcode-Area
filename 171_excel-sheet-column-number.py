class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if len(columnTitle) == 1:
            return ord(columnTitle) - 64

        n = len(columnTitle)-1
        result = 0
        for i in columnTitle:
            temp = ((ord(i) - 64) * (26**n))
            result += temp
            n -= 1
        return result


if __name__ == "__main__":
    test = Solution()
    a_columnTitle = "A"
    # Output: 1

    b_columnTitle = "AB"
    # Output: 28

    c_columnTitle = "ZY"
    # Output: 701

    print(test.titleToNumber(a_columnTitle))
    print(test.titleToNumber(b_columnTitle))
    print(test.titleToNumber(c_columnTitle))

# a_columnTitle = "A"
# print(ord(a_columnTitle)-64)
