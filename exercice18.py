def save_to_file(file_name, data):
    
        with open(file_name, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')  
        print(f"List saved to {file_name}")
    

def load_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return [int(line.strip()) for line in file.readlines()]  
    except FileNotFoundError:
        print(f"No such file: {file_name}")

numbers = [1, 2, 3, 4, 5]
while True:
    print("\nMenu:")
    print("1. Append an element.")
    print("2. Insert an element at a specific position.")
    print("3. Pop an element.")
    print("4. Remove an element.")
    print("5. Sort the list.")
    print("6. Reverse the list.")
    print("7. Search for an element.")
    print("8. Save the list to a file.")
    print("9. Load a list from a file.")
    print("10. Quit.")
    print("\nCurrent List:", numbers)

    choice = input("Choose an option: ")

    if choice == "1":
        
        value = input("Enter value to append: ")
        numbers.append(int(value))
        print("Updated List:", numbers)

    elif choice == "2": 
        value = int(input("Enter value to insert: "))
        index = int(input("Enter index to insert at: "))
        if 0 <= index <= len(numbers):
            numbers.insert(index, value)
            print("Updated List:", numbers)
        else:
            print("Invalid index! Please enter a value between 0 and", len(numbers))
            
    elif choice == "3":  
        if numbers:
            index = int(input(f"Enter index to pop (0 to {len(numbers) - 1}): "))
            if 0 <= index < len(numbers):
                    numbers.pop(index)
                    print("Updated List:", numbers)
            else:
                    print("Invalid index! Please enter a value between 0 and", len(numbers) - 1)
        else:
            print("The list is empty, nothing to pop.")

    elif choice == "4":  
        if numbers:
            value = int(input("Enter value to remove: "))
                
            if value in numbers:
                    numbers.remove(value)
                    print("Updated List:", numbers)
            else:
                    print(f"Value {value} not found in the list.")           
        else:
            print("The list is empty, nothing to remove.")

    elif choice == "5":
        numbers.sort()
        print("List sorted:", numbers)
        
    elif choice == "6":
        numbers.reverse()
        print("List reversed:", numbers)
        
    elif choice == "7":
        value = int(input("Enter value to search for: "))
        if value in numbers:
            print(f"Value {value} found at index {numbers.index(value)}.")
        else:
            print(f"Value {value} not found in the list.")
        
    elif choice == "8":
        file_name = input("Enter file name to save the list: ")
        save_to_file(file_name, numbers)
        
    elif choice == "9":
        file_name = input("Enter file name to load the list from: ")
        loaded_list = load_from_file(file_name)
        if loaded_list is not None:
            numbers = loaded_list
            print("List loaded successfully:", numbers)       

    elif choice == "10":
        print("Exiting the program.")
        break

    else:
        print("Invalid option! Please choose a valid menu option.")