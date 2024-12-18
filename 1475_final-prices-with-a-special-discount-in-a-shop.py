from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(len(prices)-1):
            temp = []
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    temp.append(prices[i] - prices[j])
                    break
            if len(temp) != 0:
                result += temp
            else:
                result.append(prices[i])
        return result + [prices[-1]]


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

    prices5 = [4, 7, 1, 9, 4, 8, 8, 9, 4]
    # Output: [3,6,1,5,0,0,4,5,4]

    print(test.finalPrices(prices1))
    print(test.finalPrices(prices2))
    print(test.finalPrices(prices3))
    print(test.finalPrices(prices4))
    print(test.finalPrices(prices5))
