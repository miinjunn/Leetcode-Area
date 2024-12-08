# I dont think I need to make solution for simple question into some complex unnecessary answer.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


if __name__ == "__main__":
    test = Solution()

    num1_a = "2"
    num2_a = "3"
    # Output: "6"

    num1_b = "123"
    num2_b = "456"
    # Output: "56088"

    print(test.multiply(num1_a, num2_a))
    print(test.multiply(num1_b, num2_b))
