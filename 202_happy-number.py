class Solution:
    def isHappy(self, n: int) -> bool:
        def kuadrat(x):
            nums = str(x)
            res = 0
            for i in nums:
                res += int(i)**2
            return res

        hasil = n
        temp = []
        while hasil != 1:
            hasil = kuadrat(hasil)
            # print(f'hasil: {hasil}')

            if hasil in temp:
                return False
            
            temp += [hasil]
            # print(f'temp: {temp}')

        return True


if __name__ == "__main__":
    test = Solution()

    n1 = 19
    # Output: true

    n2 = 2
    # Output: false

    n3 = 1111111
    # Output: true

    n4 = 7
    # Output: true

    n5 = 3
    # Output: False

    print(test.isHappy(n1))
    print(test.isHappy(n2))
    print(test.isHappy(n3))
    print(test.isHappy(n4))
    print(test.isHappy(n5))
