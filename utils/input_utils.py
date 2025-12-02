def ask_text(message):
    while True:
        user_input = input(message).strip()
        if user_input:
            return user_input
        print("Invalid input. Please enter some text.")

def ask_int(message, min_value=None, max_value=None):
    while True:
        try:
            user_input = input(message).strip()
            value = int(user_input)
            if min_value is not None and value < min_value:
                print(f"Invalid input. Please enter a number greater than or equal to {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Invalid input. Please enter a number less than or equal to {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def ask_choice(message, choices):
    while True:
        user_input = input(message).strip()
        for choice in choices:
            if user_input == str(choice):
                return choice
        print(f"Invalid choice. Please select from: {', '.join(map(str, choices))}")