# capacity = [2, 3, 4, 5]
# rocks = [1, 2, 4, 4]
# add_rock = 2
# # output: 3


capacity = [1, 2, 5, 6]
rocks = [1, 2, 4, 4]
add_rock = 3
# output: 4


def solution(capacity: list[int], rocks: list[int], add_rock: int) -> int:
    n = len(capacity)
    temp = [capacity[i] - rocks[i] for i in range(n)]
    temp.sort()
    print(temp)
    i = 0
    while add_rock != 0:
        if temp[i] == 0:
            i += 1
        else:
            temp[i] -= 1
            add_rock -= 1
    print(temp)
    return temp.count(0)


print(solution(capacity, rocks, add_rock))
