def plusOne(digits: list[int]) -> list[int]:
    if digits[-1] != 9:
        digits[-1] += 1
        return digits
    else:
        temp = str(int(''.join(map(str, digits))) + 1)
        result = [int(i) for i in temp]
        return result


digits = [1,2,3]
# digits = [4, 3, 2, 1]
# digits = [9, 9, 9]


print(plusOne(digits))