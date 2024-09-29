# Example 1:
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Example 2:
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
# ----------------------------------------------------


class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(f'{n:032b}')
        return int(n[::-1], base=2)


if __name__ == '__main__':
    n1 = 0b00000010100101000001111010011100
    n2 = 0b11111111111111111111111111111101
    oke = Solution()

    print(oke.reverseBits(n1))
    print(oke.reverseBits(n2))
