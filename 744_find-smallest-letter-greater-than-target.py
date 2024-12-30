from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # letters = sorted(set(letters))
        # print(f'letters: {letters}')
        for i in letters:
            if target < i:
                return i
        return letters[0]


if __name__ == "__main__":
    test = Solution()

    letters1 = ["c", "f", "j"]
    target1 = "a"
    # Output: "c"

    letters2 = ["c", "f", "j"]
    target2 = "c"
    # Output: "f"

    letters3 = ["x", "x", "y", "y"]
    target3 = "z"
    # Output: "x"

    print(test.nextGreatestLetter(letters1, target1))
    print(test.nextGreatestLetter(letters2, target2))
    print(test.nextGreatestLetter(letters3, target3))
