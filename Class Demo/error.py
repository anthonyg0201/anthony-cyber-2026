# While Loop (Infinite Loop)
while True:
    # Start the Block
    try:
        # User Input
        user_input = input("Enter a number: ")
        # Convert Number to Integer
        number = int(user_input)
        # Print the valid number
        print("You entered", number)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number?")