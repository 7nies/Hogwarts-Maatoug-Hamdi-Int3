def init_character(last_name, first_name, attributes):
    """
    This function initializes the character profile.
    :param last_name: string
    :param first_name: string
    :param attributes: dict
    :return: dict
    """
    character = {
        "Last Name": last_name,
        "First Name": first_name,
        "Money": 100,
        "Inventory": [],
        "Spells": [],
        "Attributes": attributes
    }
    return character

def display_character(character):
    """
    This function displays the character profile updated.
    :param character: dict
    :return: dict
    """
    print("Character profile:")
    for key in character:
        value = character[key]
        print(f"{key}: ", end="")
        if type(value) is dict:     # pr attributes
            print()
            for subkey in value:
                print(f"- {subkey}: {value[subkey]}")
        elif type(value) is list:
            if len(value) == 0:
                print()
            else:
                text_list = []
                for item in value:
                    text_list.append(str(item))
                print(", ".join(text_list))

        else:
            print(value)

def modify_money(character, amount):
    """
    This function modifies the money parameter from the character profile.
    :param character: dict
    :param amount: int
    :return: none
    """
    character["Money"] += amount

def add_item(character, key, item):
    """
    This function adds an item to either the inventory or spell parameters the character profile.
    :param character:
    :param key:
    :param item:
    :return:
    """
    character[key].append(item)
    return character
