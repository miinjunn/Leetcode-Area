# # strs = ["dog","racecar","car"]
# # strs = ["cir", "car"]
# # output: "fl"
# # minimal_loop = min(strs, key=len)

strs = ["fliwer", "flow", "flight"]

# OPTIMIZE ----------------------------------------------------
def longestCommonPrefix(strs: list) -> str:
    strs.sort()
    temp1 = strs[0]
    temp2 = strs[-1]

    res = ''
    minimal_loop = min(len(temp1), len(temp2))
    for i in range(minimal_loop):
        if temp1[i] == temp2[i]:
            res += temp1[i]
        else:
            break
    return res


print(longestCommonPrefix(strs))


# ------------------------------------------------
#     wadah = []
#     for j in strs:
#         wadah.append(j[i])
#     temp = set(wadah)
#     if len(temp) == 1:
#         res += temp
#     else:
#         break

# return ''.join(res)

# print(longestCommonPrefix(strs))
# ------------------------------------------------

# def longestCommonPrefix(strs: list) -> str:
#     minimal_loop = min(map(len, strs))
#     res = []
#     for i in range(minimal_loop):
#         wadah = []
#         for j in strs:
#             wadah.append(j[i])
#         temp = set(wadah)
#         if len(temp) == 1:
#             res += temp
#         else:
#             break

#     return ''.join(res)

# print(longestCommonPrefix(strs))

# def longestCommonPrefix(v: list) -> str:
#     ans = ""
#     v = sorted(v)
#     print(v)
#     first = v[0]
#     last = v[-1]
#     for i in range(min(len(first), len(last))):
#         if (first[i] != last[i]):
#             return ans
#         ans += first[i]
#     return ans

# strs = ["capt", "capr", 'capp']
# print(longestCommonPrefix(strs))
