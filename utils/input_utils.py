import json



def ask_text(message):
    while True:
        user_input = input(message).strip()
        if user_input:
            return user_input
        print("Invalid input. Please enter some text.")


def ask_number(message, min_val=None, max_val=None):
    valid = False
    while not valid:
        user_input = input(message).strip()

        if not user_input:      # est-ce vide ?
            print("Invalid input. Please enter a number.")
        else:                   # on vérifie si c'est négatif
            start_index = 0
            neg = False
            if user_input[0] == '-':
                neg = True
                start_index = 1

            all_int = True      # on regarde si tous les ...[i] sont des nombres
            for i in range(start_index, len(user_input)):
                if user_input[i] < '0' or user_input[i] > '9':
                    all_int = False

            if not all_int or start_index == len(user_input):
                print("Invalid input. Please enter a number.")
            else:
                value = 0       # juste la formule de la question - convertion d'Unicode en numéral
                for i in range(start_index, len(user_input)):
                    digit = ord(user_input[i]) - ord('0')
                    value = value * 10 + digit      # on décale de 1 puis on ajoute le nombre suivant

                if neg:
                    value = -value

                if min_val is not None and value < min_val:     # vérifie la rangée
                    print(f"Please enter a number between {min_val} and {max_val}.")
                elif max_val is not None and value > max_val:
                    print(f"Please enter a number between {min_val} and {max_val}.")
                else:
                    valid = True
    return value


def ask_choice(message, options):
    print(message)
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    choice = ask_number("Your choice: ", 1, len(options))
    return options[choice - 1]


def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data