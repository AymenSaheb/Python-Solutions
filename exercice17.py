numbers = []
shoe_sizes = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

print("Numbers List:", numbers)

numbers.append(1)
numbers.append(2)

print("Numbers List:", numbers)

for i in [8, 9, 10, 11, 12]:
    shoe_sizes.append(i)

print("Shoe Sizes List:", shoe_sizes)

numbers = list(set(numbers))

combined_list = numbers + shoe_sizes

print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)
print("Combined List:", combined_list)