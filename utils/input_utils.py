import json

def ask_text(message):
    """
    This function asks the user to enter some text in response to a printed message.

    :param message: string
    :return: string
    """
    while True:
        user_input = input(message).strip()
        if user_input:
            return user_input
        print("Invalid input. Please enter some text.")


def ask_number(message, min_val=None, max_val=None):
    """
    This function asks for a number, converts it to an integer and returns it.
    :param message: string
    :param min_val: int
    :param max_val: int
    :return: int
    """
    valid = False
    while not valid:
        user_input = input(message).strip()
        if not user_input:      # vide ?
            print("Invalid input. Please enter a number.")
        else:
            start_index = 0
            neg = False
            if user_input[0] == '-':
                neg = True
                start_index = 1
            all_int = True
            for i in range(start_index, len(user_input)):
                if user_input[i] < '0' or user_input[i] > '9':
                    all_int = False
            if not all_int or start_index == len(user_input):
                print("Invalid input. Please enter a number.")
            else:
                value = 0
                for i in range(start_index, len(user_input)):
                    digit = ord(user_input[i]) - ord('0')
                    value = value * 10 + digit
                if neg:
                    value = -value
                if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                    print(f"Please enter a number between {min_val} and {max_val}.")
                else:
                    valid = True
    return value


def ask_choice(message, options):
    """
    This function asks the user to choose from a list of option using the ask_number function.
    :param message: string
    :param options: list
    :return: list
    """
    print(message)
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    choice = ask_number("Your choice: ", 1, len(options))
    return options[choice - 1]

def load_file(file_path):
    """
    This function loads a json file and returns it.
    :rtype: Any
    :param file_path: string
    :return: any
    """
    with open(file_path, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data