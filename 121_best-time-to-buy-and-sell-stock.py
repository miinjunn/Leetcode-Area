from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # CARA-1 nested-loop O(n**2)-----------------------------
        # result = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         if prices[i] > prices[j]:
        #             continue
        #         temp = prices[j] - prices[i]
        #         result = max(result, temp)
        # return result

        # CARA-2 O(n)-----------------------------
        if not prices:
            return 0

        if len(set(prices)) == 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for i in prices:
            if i < min_price:
                min_price = i

            current_profit = i - min_price
            max_profit = max(max_profit, current_profit)

        return max_profit


if __name__ == "__main__":
    test = Solution()

    prices1 = [7, 1, 5, 3, 6, 4]
    # Output: 5

    prices2 = [7, 6, 4, 3, 1]
    # Output: 0

    prices3 = [7, 7, 7, 7, 7]
    # Output: 0

    prices4 = [7, 2, 6, 1, 3]
    # Output: 4

    print(test.maxProfit(prices1))
    print(test.maxProfit(prices2))
    print(test.maxProfit(prices3))
    print(test.maxProfit(prices4))
