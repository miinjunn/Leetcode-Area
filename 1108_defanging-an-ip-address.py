class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


if __name__ == "__main__":
    test = Solution()

    address1 = "1.1.1.1"
    # Output: "1[.]1[.]1[.]1"

    address2 = "255.100.50.0"
    # Output: "255[.]100[.]50[.]0"

    print(test.defangIPaddr(address1))
    print(test.defangIPaddr(address2))