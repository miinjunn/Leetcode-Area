# im sorry, this is not what the description asked
def mySqrt(x: int) -> int:
    return int(x**0.5)
# ------------------------------------------------------


# this is what the description asked
def mySqrt(x: int) -> int:
    counter = 1
    while counter * counter < x:
        counter += 1
    if counter * counter == x:
        return counter
    else:
        return counter-1


# # test
print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(1))
