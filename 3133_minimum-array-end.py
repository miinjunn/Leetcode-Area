class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # BASIC ----------------------------------------------
        # def cek_and(state: list):
        #     temp = state[0]
        #     for i in range(1, len(state)):
        #         temp &= state[i]
        #     return temp

        # result = [x]
        # for _ in range(n-1):
        #     counter = result[-1]
        #     while True:
        #         if cek_and(state=result + [counter+1]) == x:
        #             break
        #         counter += 1
        #     result.append(counter+1)

        # # print(result)
        # return result[-1]

        # BASE2 ----------------------------------------------
        # result = [x]
        # for _ in range(n-1):
        #     counter = result[-1] + 1

        #     while (counter & x) != x:
        #         counter += 1

        #     result.append(counter)

        # print(result)
        # return result[-1]

        # OPTIMIZED ----------------------------------------------
        result = x
        for _ in range(n - 1):
            result += 1
            result |= x  # Set bits in result that are set in x
            while (result & x) != x:
                result += 1
        return result


if __name__ == "__main__":
    test = Solution()

    n1 = 3
    x1 = 4
    # Output: 6

    n2 = 2
    x2 = 7
    # Output: 15

    n3 = 893
    x3 = 949
    # Output: 114677

    n4 = 6715154
    x4 = 7193485
    # Output: 55012476815

    print(test.minEnd(n1, x1))
    print(test.minEnd(n2, x2))
    print(test.minEnd(n3, x3))
    print(test.minEnd(n4, x4))
