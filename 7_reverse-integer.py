# 32bit integer:
# -2_147_483_648 __range__ 2_147_483_647

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        n = str(x)
        if n[0] == '-':
            n = n[1:]

        if n[-1] == '0':
            n = n[:-1]

        res = int(''.join(reversed(n)))
        if x < 0:
            if (res * -1) < -2_147_483_648:
                return 0
            return res * -1
        else:
            if res > 2_147_483_647:
                return 0
            return res


if __name__ == "__main__":
    test = Solution()

    x1 = 123
    # Output: 321

    x2 = -123
    # Output: -321

    x3 = 120
    # Output: 21

    x4 = 0
    # Output: 0

    x5 = 1534236469
    # Output: 0

    print(test.reverse(x1))
    print(test.reverse(x2))
    print(test.reverse(x3))
    print(test.reverse(x4))
    print(test.reverse(x5))
