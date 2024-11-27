class Solution:
    def addDigits(self, num: int) -> int:
        # Learn step by step ------------------------
        # r = num
        # while True:
        #     temp = str(r)
        #     k = sum([int(i) for i in temp])
        #     if k >= 10:
        #         r = k
        #     else:
        #         return k

        # Optimize ------------------------
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


if __name__ == "__main__":
    test = Solution()

    num1 = 38
    # Output: 2

    num2 = 0
    # Output: 0

    num3 = 55
    # Output: 1

    num4 = 77
    # Output: 5

    num5 = 18
    # Output: 9

    print(test.addDigits(num1))
    print(test.addDigits(num2))
    print(test.addDigits(num3))
    print(test.addDigits(num4))
    print(test.addDigits(num5))
