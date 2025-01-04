from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        kunci = first
        for i in encoded:
            temp = i ^ kunci
            kunci = temp
            result.append(temp)

        return result


if __name__ == "__main__":
    test = Solution()

    encoded1 = [1, 2, 3]
    first1 = 1
    # Output: [1,0,2,1]

    encoded2 = [6, 2, 7, 3]
    first2 = 4
    # Output: [4,2,0,7,4]

    print(test.decode(encoded1, first1))
    print(test.decode(encoded2, first2))
