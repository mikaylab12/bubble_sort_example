# bubble sort python program
#          11, 12, 13, 42, 63, 89
numbers = [42, 12, 13, 89, 63, 11]

for j in range (0,6):
    for i in range(0,5):
        if numbers[i] > numbers[i + 1]:
            swap = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i+1]= swap

print(numbers)


