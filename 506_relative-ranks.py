from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = []
        temp = sorted(score, reverse=True)
        
        for i in score:
            if i == temp[0]:
                result.append("Gold Medal")

            elif i == temp[1]:
                result.append("Silver Medal")

            elif i == temp[2]:
                result.append("Bronze Medal")
            else:
                result.append(str(temp.index(i)+1))

        return result



if __name__ == "__main__":  
    test = Solution()

    score1 = [5, 4, 3, 2, 1]
    # Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
    # Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

    score2 = [10, 3, 8, 9, 4]
    # Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
    # Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

    print(test.findRelativeRanks(score1))
    print(test.findRelativeRanks(score2))