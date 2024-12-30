class Solution:
    def is_prime(self, x):
        if x < 2:
            return False
        elif x == 2:
            return True
        for n in range(2, x):
            if x % n == 0:
                return False
        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        counter = 0
        for i in range(left, right+1):
            temp = bin(i).count("1")
            if self.is_prime(temp) == True:
                counter += 1
        return counter


if __name__ == "__main__":
    test = Solution()

    left1 = 6
    right1 = 10
    # Output: 4

    left2 = 10
    right2 = 15
    # Output: 5

    print(test.countPrimeSetBits(left1, right1))
    print(test.countPrimeSetBits(left2, right2))
