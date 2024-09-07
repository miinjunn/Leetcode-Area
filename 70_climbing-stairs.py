# for n = 2 ada 2 cara
# for n = 3 ada 3 cara
# for n = 4 ada 5 cara
# for n = 5 ada 8 cara
# for n = 6 ada 13 cara
# memmiliki pola seperti fibonacci

# ---------------------------------------
# TIME LIMIT EXCEEDED:
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# def climbStairs(n: int) -> int:
#     return fib(n+1)


# -----------------------------------------------------------
# TIME LIMIT EXCEEDED:
# def climbStairs(n: int) -> int:
#     if n == 0 or n == 1:
#         return 1
#     return climbStairs(n-1) + climbStairs(n-2)


# -----------------------------------------------------------
# TIME COMPLEXITY: O(1):
def climbStairs(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    # Initialize variables to store number of ways to climb i stairs
    a, b = 1, 1

    # Compute number of ways to climb i stairs
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


print(climbStairs(2))  # 2
print(climbStairs(3))  # 3
print(climbStairs(4))  # 5
print(climbStairs(6))  # 13
print(climbStairs(44))  # 1134903170
