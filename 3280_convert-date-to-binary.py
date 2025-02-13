class Solution:
    def convertDateToBinary(self, date: str) -> str:
        kalimat = date.split('-')
        for i in range(len(kalimat)):
            kalimat[i] = bin(int(kalimat[i]))[2:]
        
        return "-".join(kalimat)


if __name__ == "__main__":
    test = Solution()

    date1 = "2080-02-29"
    # Output: "100000100000-10-11101"

    date2 = "1900-01-01"
    # Output: "11101101100-1-1"

    print(test.convertDateToBinary(date1))
    print(test.convertDateToBinary(date2))
