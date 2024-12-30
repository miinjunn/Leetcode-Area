from typing import List
import random as r


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        
        result = []
        for i in range(1, n):
            result.append(i)

        result.append(-sum(result))

        return result

        
        #     if r.random not in result:
        #         result.append(i)
        
        # return result

if __name__ == "__main__":
    test = Solution()

    n1 = 5
    # Output: [-7,-1,1,3,4]

    n2 = 3
    # Output: [-1,0,1]

    n3 = 1
    # Output: [0]

    print(test.sumZero(n1))
    print(test.sumZero(n2))
    print(test.sumZero(n3))
