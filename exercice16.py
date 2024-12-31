
numbers = [1, 2, 3, 4, 5]
while True:
        index = int(input("Enter index (-1 to quit): "))
        if index == -1:
            print("Exiting the program.")
            break
        if index < 0 or index >= len(numbers):
            print(f"Invalid index! Please enter a value between 0 and {len(numbers) - 1}.")
            continue
        new_value = input("Enter new value: ")
        if not new_value.isdigit():
            print("Invalid value! Please enter a numeric value.")
            continue
        numbers[index] = int(new_value)
        print(numbers)

    