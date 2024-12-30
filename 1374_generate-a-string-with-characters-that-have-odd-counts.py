class Solution:
    def generateTheString(self, n: int) -> str:
        result = ""
        if n % 2:
            result = "a" * n
        else:
            result = "a" * (n-1) + "b"

        return result


if __name__ == "__main__":
    test = Solution()

    n1 = 4
    # Output: "pppz"

    n2 = 2
    # Output: "xy"

    n3 = 7
    # Output: "holasss"

    print(test.generateTheString(n1))
    print(test.generateTheString(n2))
    print(test.generateTheString(n3))
