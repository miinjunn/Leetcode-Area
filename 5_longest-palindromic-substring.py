# s = "babad"
s = "cbbd"
# s = "a"
# s = "ac"
# s = "bb"

# BASIC ----------------------------------------------------
# def longestPalindrome(s: str) -> str:
#     result = []
#     for i in range(len(s)):
#         for j in range(i+1, len(s)+1):
#             temp = s[i:j]
#             # print(f'{temp} --- {temp[::-1]}')
#             if temp == temp[::-1]:
#                 result.append(s[i:j])

#     return max(result, key=lambda x: len(x))


# OPTIMIZED ----------------------------------------------------
def longestPalindrome(s: str) -> str:
    n = len(s)
    start = 0
    max_len = 1

    for i in range(n):
        for j in range(2):
            low = i
            hi = i + j
            while low >= 0 and hi < n and s[low] == s[hi]:
                curr_len = hi - low + 1
                if curr_len > max_len:
                    start = low
                    max_len = curr_len
                low -= 1
                hi += 1

    return s[start:start + max_len]


print(longestPalindrome(s))
