from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        img = [i[::-1] for i in image]

        m = len(img)
        n = len(img[0])
        
        for i in range(m):
            for j in range(n):
                if img[i][j] == 1:
                    img[i][j] = 0
                else:
                    img[i][j] = 1

        return img


if __name__ == "__main__":
    test = Solution()

    image1 = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    # Output: [[1,0,0],[0,1,0],[1,1,1]]

    image2 = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    # Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

    print(test.flipAndInvertImage(image1))
    print(test.flipAndInvertImage(image2))
