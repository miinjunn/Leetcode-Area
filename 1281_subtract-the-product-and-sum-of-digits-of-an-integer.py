class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        kamus = [int(i) for i in str(n)]
        kali = 1
        for i in kamus:
            kali *= i
        tambah = sum(kamus)

        return kali - tambah


if __name__ == "__main__":
    test = Solution()

    n1 = 234
    # Output: 15

    n2 = 4421
    # Output: 21

    print(test.subtractProductAndSum(n1))
    print(test.subtractProductAndSum(n2))
