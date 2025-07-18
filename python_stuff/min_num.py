Numbers = [10, 28, 32, 42, 15, 61, 71, 18, 23, 11]

min = Numbers[0]

for num in Numbers:
    if num < min:
        min = num
print("The minimum number in the list is:", min)
