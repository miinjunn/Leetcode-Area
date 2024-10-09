from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        char_now = chars[0]
        item = 1
        for i in chars[1:]:
            if i == char_now:
                item += 1
            else:
                result.append([char_now, item])
                char_now = i
                item = 1

        result.append([char_now, item])

        # check-point
        akhir = ''
        for i in result:
            iTotal = i[1]
            if iTotal == 1:
                akhir += i[0]
            elif iTotal < 10:
                akhir += f'{i[0]}{iTotal}'
            else:
                akhir += f'{i[0]}{iTotal//10}{iTotal % 10}'
        chars[:] = [i for i in akhir]
        print(chars)
        return len([i for i in chars])


# # ----------------------------------------
if __name__ == '__main__':
    test = Solution()

    chars1 = ["a", "a", "b", "b", "c", "c", "c"]
    # Output: ["a","2","b","2","c","3"]

    chars2 = ["a"]
    # Output: ["a"]

    chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    # Output: ["a","b","1","2"].

    chars4 = ["a", "a", "a", "b", "b", "a", "a"]
    # Output: ["a","2","b","2","c","3"]

    chars5 = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]
    # Output: ["o","1","0"]

    print(test.compress(chars1))
    print(test.compress(chars2))
    print(test.compress(chars3))
    print(test.compress(chars4))
    print(test.compress(chars5))
