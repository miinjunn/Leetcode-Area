class Solution:
    # basic method ----------------------------------------
    # def fib(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     else:
    #         return self.fib(n-1) + self.fib(n-2)

    # optimized method ----------------------------------------
    def fib(self, n: int) -> int:
        f = [0, 1]

        for i in range(2, n+1):
            f.append(f[i-1] + f[i-2])

        print(f)
        return f[n]


if __name__ == "__main__":
    test = Solution()

    n1 = 2
    # Output: 1

    n2 = 3
    # Output: 2

    n3 = 4
    # Output: 3

    print(test.fib(n1))
    print(test.fib(n2))
    print(test.fib(n3))
