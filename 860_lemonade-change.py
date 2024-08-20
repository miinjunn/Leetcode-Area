# bills = [5, 5, 5, 10, 20]
# bills = [5, 5, 10, 10, 20]
# bills = [5, 5, 10, 20]
bills = [5, 10, 10]


def lemon(bills):
    moneyBox = []

    for i in range(len(bills)):
        if bills[0] != 5:
            return False

        if bills[i] == 5:
            moneyBox.append(bills[i])

        moneyBox.sort()

        temp = bills[i]
        for money in moneyBox[::-1]:

            if bills[i] - money == 0:
                continue

            if bills[i] - money >= 5:
                bills[i] -= money
                moneyBox.remove(money)
                print(f'money remove: {money}')
                print(f'moneyBox: {moneyBox}')
                print(f'bills now: {bills[i]}')
                if bills[i] == 5:
                    moneyBox.append(temp)
                    print(f'moneyBox now: {moneyBox}')
                    print(f'--------------')
        
        # print(f'######------######')
        # print(f'moneymoneymoney: {moneyBox}')
        # print(f'bilsbils: {bills[i]}')
        if bills[i] != 5:
            return False

    return True


print(lemon(bills))
