class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for i in stones:
            if i in jewels:
                counter += 1
        return counter


if __name__ == "__main__":
    test = Solution()

    jewels1 = "aA"
    stones1 = "aAAbbbb"
    # Output: 3

    jewels2 = "z"
    stones2 = "ZZ"
    # Output: 0

    print(test.numJewelsInStones(jewels1, stones1))
    print(test.numJewelsInStones(jewels2, stones2))
