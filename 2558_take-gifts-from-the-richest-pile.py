from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        counter = 0
        while counter < k:
            maksimal = max(gifts)
            idx = gifts.index(maksimal)
            gifts[idx] = (maksimal ** 0.5) // 1
            counter += 1
        return sum(gifts)


if __name__ == "__main__":
    test = Solution()

    gifts1 = [25, 64, 9, 4, 100]
    k1 = 4
    # Output: 29

    gifts2 = [1, 1, 1, 1]
    k2 = 4
    # Output: 4

    gifts3 = [1, 2, 2, 2, 2, 2, 1]
    k3 = 1000
    # Output: 7

    print(test.pickGifts(gifts1, k1))
    print(test.pickGifts(gifts2, k2))
    print(test.pickGifts(gifts3, k3))
