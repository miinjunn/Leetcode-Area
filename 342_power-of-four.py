class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        kiri = 0
        kanan = 1
        while True:
            temp = 4 ** kiri
            temp_k = 4 ** kanan
            
            if temp == n or temp_k == n:
                return True
            
            if n < temp_k:
                return False
            else:
                kiri += 1
                kanan += 1


if __name__ == "__main__":
    test = Solution()

    n1 = 16
    # Output: true

    n2 = 5
    # Output: false

    n3 = 1
    # Output: true

    print(test.isPowerOfFour(n1))
    print(test.isPowerOfFour(n2))
    print(test.isPowerOfFour(n3))
