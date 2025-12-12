def init_character(last_name, first_name, attributes):
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

def modify_money(character, amount)
    character["Money"] = character["Money"] + amount
    return character

def add_item(character, key, item):
        character[key].append(item)
    return character
