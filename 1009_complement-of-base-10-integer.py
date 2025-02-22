class Solution:
    def bitwiseComplement(self, n: int) -> int:
        temp = bin(n)[2:]
        res = ""
        for i in range(len(temp)):
            if temp[i] == '1':
                res += '0'
            else:
                res += '1'

        return int(res, base=2)


if __name__ == "__main__":
    test = Solution()

    n1 = 5
    # Output: 2

    n2 = 7
    # Output: 0

    n3 = 10
    # Output: 5

    print(test.bitwiseComplement(n1))
    print(test.bitwiseComplement(n2))
    print(test.bitwiseComplement(n3))
