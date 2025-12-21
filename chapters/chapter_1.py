from universe.character import *
from utils.input_utils import *

def introduction():
    """
    This function displays the introduction for chapter 1.
    """
    print("For years, you've lived in the cupboard under the stairs at 4 Privet Drive,")
    print("with your Aunt Petunia, Uncle Vernon, and their spoiled son Dudley.")
    print()
    print("But you've never felt quite... ordinary.")
    print()
    print("Strange things have always happened around you.")
    print("Things you couldn't explain...")
    print()
    input("Press Enter to continue...")
    print()

    print("Glass vanishing at the zoo.")
    print("Your hair growing back overnight after a bad haircut.")
    print("Somehow ending up on the school roof when running from bullies.")
    print()
    print("The Dursleys pretend not to notice. Or maybe they just don't want to.")
    print()
    print("But tonight... tonight is different.")
    print()
    input("Press Enter to continue...")
    print()

    print("The clock strikes 12. Midnight arrives.")
    print("You're lying in your cupboard, listening to Dudley snoring upstairs, when you hear it.")
    print("Tap. Tap. Tap.")
    print()
    print("Something is pecking at the window.")
    print()
    input("Press Enter to continue...")
    return ''

######################################################################################
######################################################################################

def create_character():
    """
    This function aims to regroup the necessary information to the character creation through multiple scenarios (owl for the name, magic crystal for attributes).
    :return: dict
    """
    print()
    print("=" * 80)
    print("                      The letter arrives...")
    print("                             and destiny is already sealed.")
    print("=" * 80)
    print()

    print("You crawl out of your cupboard and peer through the darkness.")
    print()
    print("At the window sits a magnificent tawny owl, its amber eyes fixed on you.")
    print("In its beak is a thick envelope made of yellowish parchment.")
    print()
    print("The owl taps the window again, more insistently.")
    print()
    print("You glance toward the stairs... Everyone's asleep. You carefully open the window.")
    print()
    print("The owl swoops in silently and drops the letter into your hands.")
    print()
    input("Press Enter to continue...")
    print()

    print("You break the seal carefully. Inside, you find two items:")
    print()
    print("A formal letter on thick parchment...")
    print("And a ticket made of golden cardstock with elegant lettering.")
    print()
    print("But something's odd... The name section on the ticket is blank.")
    print()
    print("As you touch the empty space, golden ink appears, forming words:")
    print()
    print('"Write your full name upon this ticket.')
    print('Once written, your place at Hogwarts is secured."')
    print()
    print("The blank spaces seem to shimmer, waiting...")
    print()

    last_name = ask_text("Write your last name on the ticket:   ")
    first_name = ask_text("Write your first name on the ticket:   ")

    print()
    print("The moment you finish writing, the golden ink absorbs your words.")
    print("They reappear in beautiful, flowing script:")
    print()
    print("-" * 50)

    print("  ◞———————————————————————————————————————————◟")
    print("  |          ~ HOGWARTS EXPRESS ~        :     |")
    print(f"  |          For:    {first_name}  {last_name}        :     |")
    print("  |              Platform 9¾             :     |")
    print("  |         September 1st, 11:00 AM      :     |")
    print("  ◝———————————————————————————————————————————◜")

    print("-" * 50)
    print()
    print("The ticket glows briefly, then settles. It's official now.")
    print()
    input("Press Enter to continue...")
    print()

    print("Suddenly, something small and crystalline falls out of the envelope.")
    print()
    print("It's a perfectly smooth crystal, no bigger than a marble, that shifts through colors...")
    print("...like a tiny rainbow trapped in glass.")
    print()
    input("Press Enter to continue...")
    print()

    print("You place the crystal in your palm. It immediately begins to pulse with light.")
    print()
    print("=" * 80)
    print("                              The Prism of Truth")
    print("=" * 80)
    print()
    print("The crystal's voice echoes in your mind...:")
    print()
    print('"I can see who you truly are.')
    print('Answer honestly, for I will measure the four qualities')
    print('that define every witch and wizard at Hogwarts:')
    print('courage, intelligence, loyalty and ambition."')
    print()
    print("You must answer with a number between 1 and 10.")
    print()
    input("Press Enter to continue...")
    print()

    print("The crystal glows RED, warm like courage itself...")
    courage = ask_number('"How brave are you when facing the unknown?"   ',
                         1, 10)
    print()

    print("The crystal shifts to BLUE, cool like a vast library...")
    intelligence = ask_number('"How sharp is your mind? How deep is your thirst for knowledge?"   ',
                              1,10)
    print()

    print("The crystal turns YELLOW, steady like the sun...")
    loyalty = ask_number('"How loyal are you to those you care about?"   ',
                         1,10)
    print()

    print("The crystal gleams GREEN, bright like ambition's fire...")
    ambition = ask_number('"How determined are you to achieve your goals and prove your worth?"   ',
                          1,10)
    print()

    print("The Prism flashes brilliantly, then settles into a soft glow.")
    print()
    print('"The Sorting Hat will find you most interesting indeed..."')
    print()
    print("The crystal goes dark and crumbles into harmless sparkles that fade away.")
    print()

    attributes = {
        "Courage": courage,
        "Intelligence": intelligence,
        "Loyalty": loyalty,
        "Ambition": ambition
    }

    character = init_character(last_name, first_name, attributes)

    print()
    print("=" * 80)
    print("                                 Your Profile")
    print("." * 80)
    display_character(character)
    print("=" * 80)
    print()
    input("Press Enter to continue...")
    print()
    return character

######################################################################################
######################################################################################

def receive_letter(character):
    """
    This function simulates the player's reading of the Hogwarts invitation letter, issuing in either a refusal or the acceptance.
    """

    print("You can hear the blood rushing through your veins.")
    print()
    print("Your eyes go back to the letter on the floor.")
    print("You unfold the letter with trembling hands:")
    print()
    print("-" * 80)
    print("                               HOGWARTS SCHOOL")
    print("                         of WITCHCRAFT and WIZARDRY")
    print()
    print(f"Dear {character["Last Name"]} {character["First Name"]},")
    print()
    print("We are pleased to inform you that you have been accepted to")
    print("Hogwarts School of Witchcraft and Wizardry.")
    print()
    print("Please find enclosed a list of all necessary books and equipment.")
    print("Term begins on September 1st. We await your owl by no later")
    print("than July 31st.")
    print()
    print("Yours sincerely,")
    print("Minerva McGonagall")
    print("Deputy Headmistress")
    print()
    print("-" * 80)
    print()
    input("Press Enter to continue...")
    print()

    print("You stare at the letter, heart pounding.")
    print()
    print("Magic. Real magic. You're not strange...")
    print("...you're a wizard.")
    print()
    print("A wizard!")
    print()
    print("Uncle Vernon would explode if he saw this. Aunt Petunia would faint.")
    print("Dudley would probably try to eat it.")
    print()

    choice = ask_choice("Do you accept this invitation to go to Hogwarts?",
                        ["Yes, of course!", "No, I'd rather stay with Uncle Vernon..."])
    if choice == "No, I'd rather stay with Uncle Vernon...":
        print()
        print("You tear up the letter.")
        print()
        print("The magical world will never know you existed...")
        print("and the cupboard under the stairs has never felt more... permanent.")
        exit()
    else:
        print()
        print("You clutch the letter to your chest, a grin spreading across your face.")
        print('"Yes," you whisper to the empty room. "Yes, I\'m going to Hogwarts."')
        print()

    print("You hide the envelope under your thin mattress, mind racing.")
    print("How will you get to this school? Where even IS Hogwarts?")
    print()
    print("As if an answer, you hear it:")
    print("*BOOM BOOM BOOM*")
    print()
    print("Someone is pounding on the front door.")
    print()
    input("Press Enter to continue...")
    print()

def meet_hagrid():
    """
    Introduction to Hagrid and transition to shopping.
    """
    print("-" * 80)
    print("                            The Keeper of Keys")
    print("-" * 80)
    print()

    print("The pounding continues. You hear Uncle Vernon thundering down the stairs,")
    print('shouting about "the middle of the night" and "decent people."')
    print()
    print("The door rattles on its hinges.")
    print()
    print("*CRASH*")
    print()
    print("The door flies open, while Vernon didn't even have the time to unlock it.")
    print()
    print("Standing in the doorway is the largest man you've ever seen.")
    print("He's almost twice as tall as a normal person and at least five times as wide.")
    print("He has a wild, tangled beard and hair,")
    print("and beetle-black eyes that gleam with kindness.")
    print()
    print('"Sorry \'bout that," the giant says, easily bending the door back into place as if it were cardboard.')
    print()
    input("Press Enter to continue...")
    print()

    print("Uncle Vernon appears, purple-faced and trembling.")
    print("Standing bolt upright, frozen like a statue.")
    print()
    print("The big man's eyes land on you, and his whole face lights up.")
    print()
    print('"Blimey, is that really you? My, you\'ve grown!"')
    print('"Rubeus Hagrid, Keeper of Keys and Grounds at Hogwarts School of')
    print('Witchcraft and Wizardry. But everyone calls me Hagrid."')
    print()
    print("His handshake nearly crushes your fingers.")
    print()
    print('"Got your letter, did ya? Good, good! Dumbledore sent me')
    print('to make sure you got it and to help ya get your school things."')
    print()
    input("Press Enter to continue...")
    print()

    print('"Right then! We\'ve got a lot to do and not much time.')
    print('Gotta get ya to Diagon Alley, the shoppin\' district for magical folk."')
    print()
    print("Hagrid notices your lack of visible emotions.")
    print('"Now, ready for your first taste o\' the magical world?"')
    print()

    choice = ask_choice("Will you follow Hagrid?",
               ["Yes", "No"])
    if choice=="No":
        print('You hesitate. "I... I don\'t know..."')
        print()
        print("Hagrid smiles so much his eyes close.")
        print('"I like your spirit, but we\'ve got supplies to buy before September!"')
        print()
        print("He carries you over his shoulder and you both disappear into the night,")
        print("under the eyes of your uncle - the only thing that still moves in him.")
    else:
        print('"Excellent!" Hagrid booms. "That\'s the spirit. Come on then!"')
        print("Hagrid leads you out into the night. The Dursleys don't even try to stop you.")
    print()
    input("Press Enter to continue...")
    print()

def buy_supplies(character):
    """
    This function serves for the player to buy supplies to their character, with a story part followed by a shopping part.
    In the shopping part, the inventory.json file is called.
    :param character:
    :return:
    """
    print("="*80)
    print("                                 Diagon Alley")
    print("="*80)
    print()

    print('"How do we get there?" you ask.')
    print()
    print("He pulls out a pink umbrella, which appears absurdly small in his massive hands,")
    print("and taps a specific rhythm on a nearby brick wall:")
    print("Tap-tap. Tap. Tap-tap-tap.")
    print()
    print("The bricks shifts, folding away to reveal a narrow")
    print("cobblestone alley lit by flickering lanterns. Even at night, you can see")
    print("some shops till open, their windows glowing with magical light,")
    print("displaying everything from bubbling cauldrons")
    print("to broomsticks that twitch as if eager to fly.")
    print()
    print('"Welcome," Hagrid says proudly, "to Diagon Alley."')
    print()
    print("Shop signs creak in the breeze.")
    print()
    input("Press Enter to continue...")
    print()

    print('"Now, first things first. You\'ll need money.')
    print("Hagrid reaches into his coat and pulls out a leather pouch that jingles.")
    print('"Dumbledore gave me some to get ya started.')
    print('You\'ve got 100 Galleons here ; that\'s wizard money."')
    print()
    print("He hands you the pouch. The coins inside are shining gold.")
    print()
    print('"Right! Let\'s get your supplies. You\'ve got a list in that letter, didn\'t ya?')
    print('Three things you absolutely MUST buy or you can\'t attend Hogwarts:')
    print('a wand, robes, and your potions book. Everything else is optional but useful."')
    print()
    input("Press Enter to continue...")
    print()

    print("A shop door opens, and a witch in midnight-blue robes steps out.")
    print("She's holding what looks like a compass, except the needle is pointing at you.")
    print()
    print('"New student... Let me help you navigate the shops that are still open."')
    print()
    print("She waves her wand, and a shimmering golden map appears in the air,")
    print("showing all the shops in Diagon Alley.")
    print()
    input("Press Enter to continue...")
    print()

    print("-" * 80)
    print("                              Running errands...")
    print("-" * 80)
    print("Catalog of available items:")

    # Load inv + req items
    inv = load_file("data/inventory.json")
    req_items = ["Magic Wand", "Wizard Robe", "Potions Book"]

    # Print the shop UI
    print("." * 50)
    for key in inv:
        req = ""
        item_name = inv[key][0]
        item_price = inv[key][1]
        if item_name in req_items:
            req = " (required)"
        print(f"{key}. {item_name} - {item_price} Galleons{req}")
    print("." * 50)
    print()

    # Remaining money
    print(f"You have {character['Money']} Galleons.")
    print(f"Remaining required items: {', '.join(req_items)}")
    print()

    # Buy as long as there are still req items
    while len(req_items) > 0:
        choice = ask_number("Enter the number of the item to buy: ", 1, len(inv))

        # Convert choice to string to match dictionary keys
        choice_key = str(choice)

        # Get item details
        item_name = inv[choice_key][0]
        item_price = inv[choice_key][1]

        # Check if already in char inv
        if item_name in character["Inventory"]:
            print(f"You already have {item_name}.")
            print()
            continue  # Skip to next iteration

        # Check if player can afford
        if character["Money"] < item_price:
            print()
            print("You don't have enough money!")
            print()
            print('Hagrid shakes his head sadly. "Can\'t go to Hogwarts without the essentials."')
            print()
            print("Game over: Insufficient funds for required supplies.")
            exit(0)

        # Purchase item
        modify_money(character, -item_price)
        add_item(character, "Inventory", item_name)
        print(f"You bought: {item_name} (-{item_price} Galleons).")
        print(f"You have {character['Money']} Galleons.")

        # Remove from required list if it was required
        if item_name in req_items:
            req_items.remove(item_name)

        # Display remaining required items
        if len(req_items) > 0:
            print(f"Remaining required items: {', '.join(req_items)}")
        else:
            print("All required items have been purchased!")
        print()
    print("-"*80)
    print()
    input("Press Enter to continue...")
    print()

    # Transition
    print()
    print('"Perfect!" the witch says. "Now, every Hogwarts student needs')
    print('a loyal companion."')
    print()
    print("She gestures toward a shop where soft hoots, meows, squeaks, and croaks")
    print("can be heard.")
    print()
    input("Press Enter to continue...")
    print()

    print("-"*80)
    print("                              Magical Menagerie")
    print("-"*80)
    print()

# Print pet store UI
    print("Available pets:")
    print("."*50)
    print("1. Owl - 20 Galleons (Delivers mail and very intelligent)")
    print("2. Cat - 15 Galleons (Independent and excellent at catching pests)")
    print("3. Rat - 10 Galleons (Low maintenance and surprisingly clever)")
    print("4. Toad - 5 Galleons (Traditional and brings good luck)")
    print("."*50)
    print()

    pets = {
        "Owl": 20,
        "Cat": 15,
        "Rat": 10,
        "Toad": 5
    }

    pet_choice = ask_choice("Which pet do you want?", ["Owl", "Cat", "Rat", "Toad"])
    pet_price = pets[pet_choice]

    # Check if enough money for pet
    if character["Money"] < pet_price:
        print()
        print(f"You don't have enough money for a {pet_choice}!")
        print("Without a pet, you cannot attend Hogwarts...")
        print("Hagrid looks disappointed as you realize you've spent your money unwisely.")
        print()
        print("Game over...")
        exit()

    # Buy the pet
    modify_money(character, -pet_price)
    add_item(character, "Inventory", pet_choice)

    print()
    print(f"You chose: {pet_choice} (-{pet_price} Galleons).")
    print()
    input("Press Enter to continue...")
    print()

    print("You emerge from the shops, arms full of supplies and your new companion")
    print("at your side. Hagrid beams at you.")
    print()
    print('"All set then? Got everything ya need?"')
    print()
    print("You nod, still hardly believing this is real.")
    print()
    print("All required items have been successfully purchased! Here is your")
    print("final inventory:")
    print()

    print()
    print("=" * 80)
    print("                                 Your Profile")
    print("." * 80)
    display_character(character)
    print("=" * 80)
    print()
    input("Press Enter to continue...")
    print()
    return character


def start_chapter_1():
    """
    This function regroups the entirety of the function that form chapter 1, as well as a small conclusion.
    :return:
    """
    print("~"*80)
    print("=" * 80)
    print("                    Chapter I: Fall into the magical world")
    print("=" * 80)
    print("~"*80)
    print()

    introduction()
    char = create_character()
    receive_letter(char)
    meet_hagrid()
    buy_supplies(char)

    print("=" * 80)
    print()


    print()
    input("Press Enter to continue...")
    print()
    return char