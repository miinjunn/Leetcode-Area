from collections import Counter


class Solution:
    def greatestLetter(self, s: str) -> str:
        result = ""
        s = set(s)
        for i in s:
            if i.islower() == True:
                if i.upper() in s:
                    result += i
            else:
                if i.lower() in s:
                    result += i

        return max(result).upper() if len(result) != 0 else result


if __name__ == "__main__":
    test = Solution()

    s1 = "lEeTcOdE"
    # Output: "E"

    s2 = "arRAzFif"
    # Output: "R"

    s3 = "AbCdEfGhIjK"
    # Output: ""

    print(test.greatestLetter(s1))
    print(test.greatestLetter(s2))
    print(test.greatestLetter(s3))
