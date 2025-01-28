from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start < destination:
            res_kiri = sum(distance[start:destination])
        else:
            res_kiri = sum(distance[destination:start])

        # print(f'res_kiri: {res_kiri}')

        res_kanan = sum(distance) - res_kiri
        # print(f'res_kanan: {res_kanan}')

        return min(res_kiri, res_kanan)


if __name__ == "__main__":
    test = Solution()
    distance1 = [1, 2, 3, 4]
    start1 = 0
    destination1 = 1
    # Output: 1

    distance2 = [1, 2, 3, 4]
    start2 = 0
    destination2 = 2
    # Output: 3

    distance3 = [1, 2, 3, 4]
    start3 = 0
    destination3 = 3
    # Output: 4

    distance4 = [7, 10, 1, 12, 11, 14, 5, 0]
    start4 = 7
    destination4 = 2
    # Output: 4

    print(test.distanceBetweenBusStops(distance1, start1, destination1))
    print(test.distanceBetweenBusStops(distance2, start2, destination2))
    print(test.distanceBetweenBusStops(distance3, start3, destination3))
    print(test.distanceBetweenBusStops(distance4, start4, destination4))
