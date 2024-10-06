class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        result = []
        for i in candies:
            if i+extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result


if __name__ == '__main__':
    test = Solution()
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    # Output = [true,true,true,false,true]

    candies2 = [4, 2, 1, 1, 2]
    extraCandies2 = 1
    # Output = [true,false,false,false,false]

    candies3 = [12, 1, 12]
    extraCandies3 = 10
    # Output = [true,false,true]

    print(test.kidsWithCandies(candies, extraCandies))
    print(test.kidsWithCandies(candies2, extraCandies2))
    print(test.kidsWithCandies(candies3, extraCandies3))
