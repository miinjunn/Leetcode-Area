class Solution:
    def findComplement(self, num: int) -> int:
        res = ""
        temp = bin(num)[2:]
        for i in range(len(temp)):
            if temp[i] == '1':
                res += '0'
            else:
                res += '1'
        return int(res, base=2)


if __name__ == "__main__":
    test = Solution()

    num1 = 5
    # Output: 2

    num2 = 1
    # Output: 0

    num3 = 6
    # Output: 0

    print(test.findComplement(num1))
    print(test.findComplement(num2))
    print(test.findComplement(num3))
