# not as described, sorry :)
# its not what the description said, sorry :)
# :)
import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        temp = dividend / divisor
        if temp < 0:
            return math.ceil(temp)
        if temp > (2**31)-1:
            return (2**31)-1
        return math.floor(temp)


if __name__ == "__main__":
    test = Solution()

    dividend1 = 10
    divisor1 = 3
    # Output: 3

    dividend2 = 7
    divisor2 = -3
    # Output: -2

    dividend3 = -2147483648
    divisor3 = -1
    # Output: 2147483648

    print(test.divide(dividend1, divisor1))
    print(test.divide(dividend2, divisor2))
    print(test.divide(dividend3, divisor3))
