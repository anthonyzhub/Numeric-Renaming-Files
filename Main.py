import os

if __name__ == "__main__":
    
    # Specify directory
    current_directory = "/Users/anthonyzhub/Downloads/"

    # List all files in directory
    list_directory = []
    for item in os.listdir(current_directory):

        # If item is a file and not hidden, add it to list
        if os.path.isfile(current_directory + item) and not item.startswith("."):

            # Add to list
            list_directory.append(item)

            # Print recently added item
            print(item)

    # Sort list for further use
    list_directory = sorted(list_directory)
    
    # Ask for new name
    user_input = input("Enter new name and extension (use # for numeric value): ")
    user_value = input("Enter starting value: ")

    # Convert user_value to int
    if user_value.isnumeric():
        user_value = int(user_value)
    else:
        print("You did not enter a numeric value!\nAborting...")
        exit()

    # Iterate word to find pound symbol
    for element in list_directory:

        # Need to specify full path for old and new file's name
        os.rename(current_directory + element, current_directory + user_input.replace("#", str(user_value)))
        user_value += 1

    print("\nDone!")

    
