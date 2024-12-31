
def save_to_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            for num in data:
                file.write(str(num) + '\n')
        print(f"List saved to {file_name}")
    except Exception as e:
        print(f"Error saving to file: {e}")



def sorted_list_builder():
    user_list = []

    while True:
            number = input("Enter a number (enter 0 to stop): ").strip()
            if number == '0':
                break

          
            number = int(number)

         
            user_list.append(number)

      
            print(f"Current List: {user_list}")
            print(f"Sorted List: {sorted(user_list)}")
    
    
    save_choice = input("Do you want to save the list to a file? (yes/no): ").strip().lower()
    if save_choice == "yes":
        file_name = input("Enter the file name to save the list: ").strip()
        save_to_file(file_name, user_list)

    print(f"List in Descending Order: {sorted(user_list, reverse=True)}")


sorted_list_builder()
