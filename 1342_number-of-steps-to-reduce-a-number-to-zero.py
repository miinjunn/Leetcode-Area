num = 123
counter = 0
while num != 0:
    if num % 2:
        num -= 1
    else:
        num /= 2
    counter += 1


print(counter)
