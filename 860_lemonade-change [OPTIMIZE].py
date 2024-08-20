bills = [5, 5, 5, 10, 20]
# bills = [5, 5, 10, 10, 20]
# bills = [5, 5, 10, 20]
# bills = [5, 10, 10]


def lemonadeChange(bills):
    moneyBox = {5: 0,
                10: 0,
                20: 0}

    for pembeli in bills:
        if pembeli == 5:
            moneyBox[5] += 1

        elif pembeli == 10:
            if moneyBox[5] > 0:
                moneyBox[5] -= 1
                moneyBox[10] += 1
            else:
                return False

        elif pembeli == 20:
            if (moneyBox[5] > 0) and (moneyBox[10] > 0):
                moneyBox[5] -= 1
                moneyBox[10] -= 1

            elif moneyBox[5] >= 3:
                moneyBox[5] -= 3

            else:
                return False

    return True


print(lemonadeChange(bills))
