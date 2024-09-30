class Solution:
    def myPow(self, x: float, n: int) -> float:
        return (x ** n)


if __name__ == '__main__':
    test = Solution()
    x1, n1 = 2.00000, 10
    x2, n2 = 2.10000, 3
    x3, n3 = 2.00000, -2

    print(test.myPow(x1, n1))
    print(test.myPow(x2, n2))
    print(test.myPow(x3, n3))
