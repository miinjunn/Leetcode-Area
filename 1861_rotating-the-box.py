from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # BASIC ------------------------------------------------------------------
        # m = len(box[0])
        # n = len(box)
        # for i in range(n):
        #     for _ in range(m):
        #         for j in range(len(box[i]) - 1):
        #             if box[i][j] == '#' and box[i][j + 1] == '.':
        #                 box[i][j] = '.'
        #                 box[i][j + 1] = '#'
        #             elif box[i][j] == '*' or box[i][j] == '*':
        #                 continue
        # box[:] = box[::-1]

        # # -----------Transpose-----------
        # mtx = []
        # for i in range(m):
        #     temp = []
        #     for j in range(n):
        #         temp.append(box[j][i])
        #     mtx.append(temp)
        # return mtx

        # OPTIMIZED ------------------------------------------------------------------
        m = len(box[0])
        n = len(box)

        for i in range(n):
            write_pointer = m - 1
            for j in range(m - 1, -1, -1):
                if box[i][j] == '#':
                    box[i][write_pointer] = '#'
                    if write_pointer != j:
                        box[i][j] = '.'
                    write_pointer -= 1
                elif box[i][j] == '*':
                    write_pointer = j - 1
        box.reverse()

        mtx = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(box[j][i])
            mtx.append(temp)
        return mtx


if __name__ == "__main__":
    test = Solution()

    box1 = [["#", ".", "#"]]
    # Output: [["."],
    #          ["#"],
    #          ["#"]]

    box2 = [["#", ".", "*", "."],
            ["#", "#", "*", "."]]
    # Output: [["#","."],
    #         ["#","#"],
    #         ["*","*"],
    #         [".","."]]

    box3 = [["#", "#", "*", ".", "*", "."],
            ["#", "#", "#", "*", ".", "."],
            ["#", "#", "#", ".", "#", "."]]
    # Output: [[".","#","#"],
    #         [".","#","#"],
    #         ["#","#","*"],
    #         ["#","*","."],
    #         ["#",".","*"],
    #         ["#",".","."]]

    print(test.rotateTheBox(box1))
    print(f'\n{test.rotateTheBox(box2)}')
    print(f'\n{test.rotateTheBox(box3)}')
