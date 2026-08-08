# Day 01 - Python Lists

numbers = [10, 20, 30, 40, 50]

# Indexing
print(numbers[0])
print(numbers[4])

# Changing a value
numbers[1] = 99
print(numbers)

# append()
numbers.append(60)
print(numbers)

# insert()
numbers.insert(2, 25)
print(numbers)

# remove()
numbers.remove(25)
print(numbers)

# pop()
numbers.pop()
print(numbers)

# length
print(len(numbers))

# Loop through a list
for number in numbers:
    print(number)

# Sum of numbers
total = 0

for number in numbers:
    total = total + number

print("Total:", total)

# Count even numbers
count = 0

for number in numbers:
    if number % 2 == 0:
        count = count + 1

print("Even numbers:", count)

# Find largest number
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)

# Find smallest number
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest:", smallest)
