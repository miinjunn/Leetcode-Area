from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i = 0
        j = 1
        n = len(prices)
        m = min(prices)
        while j < n:
            if prices[i] < min(prices[i+1:]):
                continue
            if j > i and prices[j] <= prices[i]:
                prices[i] -= prices[j]
                i += 1
                j = i+1
            else:
                j += 1
        return prices


if __name__ == "__main__":
    test = Solution()

    prices1 = [8, 4, 6, 2, 3]
    # Output: [4,2,4,2,3]

    prices2 = [1, 2, 3, 4, 5]
    # Output: [1,2,3,4,5]

    prices3 = [10, 1, 1, 6]
    # Output: [9,0,1,6]

    prices4 = [8, 7, 4, 2, 8, 1, 7, 7, 10, 1]
    # Output: [1,3,2,1,7,0,0,6,9,1]

    prices5 = [3, 6, 1, 9, 4, 8, 8, 9, 4]
    # Output: [1,3,2,1,7,0,0,6,9,1]

    # print(test.finalPrices(prices1))
    # print(test.finalPrices(prices2))
    # print(test.finalPrices(prices3))
    print(test.finalPrices(prices4))
