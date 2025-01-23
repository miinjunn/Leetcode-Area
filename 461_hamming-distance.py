class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xx = bin(x)[2:]
        yy = bin(y)[2:]
        temp = max(len(xx), len(yy))
        while len(xx) < temp:
            xx = '0' + xx

        while len(yy) < temp:
            yy = '0' + yy

        counter = 0
        for i in range(len(xx)):
            if xx[i] != yy[i]:
                counter += 1

        return counter


if __name__ == "__main__":
    test = Solution()

    x1 = 1
    y1 = 4
    # Output: 2

    x2 = 3
    y2 = 1
    # Output: 1

    x3 = 2
    y3 = 5
    # Output: 3

    # 0010
    # 0101
    # 0111
    print(test.hammingDistance(x1, y1))
    print(test.hammingDistance(x2, y2))
    print(test.hammingDistance(x3, y3))
