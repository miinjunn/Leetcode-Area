from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahr = celsius * 1.80 + 32.00
        # return [f'{kelvin:.2f}', f'{fahr:.2f}']
        return kelvin, fahr


if __name__ == "__main__":
    test = Solution()

    celsius1 = 36.50
    # Output: [309.65000,97.70000]

    celsius2 = 122.11
    # Output: [395.26000,251.79800]

    print(test.convertTemperature(celsius1))
    print(test.convertTemperature(celsius2))
