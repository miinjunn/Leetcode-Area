from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 2:
            res += [[1, 1]]
            return res

        for i in range(2, numRows):
            if i == 2:
                res.append([1, 1])

            temp = res[-1]
            k = [1]
            for i in range(len(temp)-1):
                k.append(temp[i] + temp[i+1])
            k.append(1)
            res.append(k)
        return res


if __name__ == "__main__":
    test = Solution()

    numRows1 = 5
    # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    numRows2 = 1
    # Output: [[1]]

    print(test.generate(numRows1))
    print(test.generate(numRows2))
    print(test.generate(numRows=2))

    # print(test.generate(numRows=10))
    # print(test.generate(numRows=30))
