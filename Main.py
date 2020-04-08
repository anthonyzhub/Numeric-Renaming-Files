import os
import sys
import re

def to_int(curr_string):

    # OBJECTIVE: Check if string is a digit or not
    
    # Check if string is numeric or not
    if curr_string.isdigit():
        return int(curr_string)
    else:
        return curr_string

def natural_keys(curr_string):

    # OBJECTIVE: Turn string into a list of string and numbers

    # Create new list for future return
    new_string = []

    # Split string by separating characters from digits
    # (\d+) means find 1 or more digits in string
    # EX. "ab123z" -> "ab", "123", "z"
    for character in re.split(r'(\d+)', curr_string):

        # Change "character" to int
        # and append it to list
        new_string.append(to_int(character))

    # Return list
    return new_string

def print_list(curr_list):

    # OBJECTIVE: Prints all elements inside the list

    for i in curr_list:
        print(i)

if __name__ == "__main__":

    # Accept command-line input
    if len(sys.argv) != 2:
        print("Invalid input!\nFollow guidelines: python3 Main.py <directory's path>")
        exit()
    
    # Add last command-line argument to current_directory
    current_directory = sys.argv[-1]

    # Add forward slash to "current_directory" if it doesn't have it
    if not current_directory[-1] == "/":
        current_directory += "/"

    # If path doesn't exist and is not a directory, exit program
    if not os.path.exists(current_directory) and not os.path.isdir(current_directory):
        print("Invalid directory!")
        exit()

    # List all files in directory
    list_directory = []
    for file in os.listdir(current_directory):

        # Create string of file's full path
        current_full_path = current_directory + file

        # If item is not a directory and is not hidden, then add to list
        if not os.path.isdir(current_full_path) and not file.startswith("."):

            # Add to list
            list_directory.append(current_full_path)

    # Sort list with custom function
    list_directory.sort(key=natural_keys)
    
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
    for old_path in list_directory:

        # Need to specify full path for old and new file's name
        # os.rename(old name, new name)
        new_path = current_directory + user_input.replace("#", str(user_value))
        os.rename(old_path, new_path)
        
        # Increment value for ascending order
        user_value += 1

    print("\nDone!")
    
