class Solution:
    def hammingWeight(self, n: int) -> int:
        # cara-1 -------------
        result = bin(n)[2:]
        return result.count('1')

        # cara-2 -------------
        res = 0
        while n:
            res += (n%2)
            print(f'res: {res}')
            n = n//2
            print(f'n: {n}\n')
        return res

if __name__ == "__main__":
    test = Solution()

    n1 = 11
    # Output: 3

    n2 = 128
    # Output: 1

    n3 = 2147483645
    # Output: 30

    print(test.hammingWeight(n1))
    print(test.hammingWeight(n2))
    print(test.hammingWeight(n3))
