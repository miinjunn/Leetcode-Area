# flowerbed = [0, 1, 0]
flowerbed = [0]
# flowerbed = [1, 0, 0, 0, 0, 1]
n = 1


def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if n > flowerbed.count(0):
        return False

    flowerbed = [0] + flowerbed + [0]
    for i in range(1, len(flowerbed)-1):
        print(f'i: {i}')

        if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and n != 0:
            print('b')
            flowerbed[i] = 1
            n -= 1
    print('-------------------------')
    print(f'n: {n}')
    print(f'flowerbeds: {flowerbed}')

    if n == 0:
        return True
    else:
        return False


print(canPlaceFlowers(flowerbed, n))
