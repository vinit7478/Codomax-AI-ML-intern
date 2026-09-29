numbers = [12, 45, 7, 32, 19]
largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

for number in numbers:
    if number < smallest:
        smallest = number

print("Largest number is", largest)
print("Smallest number is", smallest)
