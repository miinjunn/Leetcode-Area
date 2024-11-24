# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # act this is isBadVersion():
    def isBadVersion(self, version, bad):
        return version >= bad

    # basic method ---------------------------------------
    # def firstBadVersion(self, n: int, bad: int) -> int:
        # awal = 1
        # if n < 2:
        #     akhir = 1
        # else:
        #     akhir = (n//2) + 1

        # while True:
        #     for i in range(awal, akhir+1):
        #         if self.isBadVersion(i, bad):
        #             return i
        #     awal = akhir + 1
        #     akhir = awal + ((n-akhir)//2)

    # optimize ---------------------------------------
    def firstBadVersion(self, n: int, bad: int) -> int:
        awal = 1
        akhir = n

        while awal < akhir:
            mid = awal + (akhir - awal) // 2
            if self.isBadVersion(mid, bad):
                akhir = mid
            else:
                awal = mid + 1
        return awal


if __name__ == "__main__":
    test = Solution()

    n1 = 5
    bad1 = 4
    # Output: 4

    n2 = 1
    bad2 = 1
    # Output: 1

    n3 = 2126753390
    bad3 = 1702766719

    print(test.firstBadVersion(n1, bad1))
    print(test.firstBadVersion(n2, bad2))
    print(test.firstBadVersion(n3, bad3))
