
def addBinary(a: str, b: str) -> str:
    result = int(a, 2) + int(b, 2)
    return str(bin(result))[2:]


# a = "1010"
# b = "1011"
a = "11"
b = "1"


print(addBinary(a, b))
