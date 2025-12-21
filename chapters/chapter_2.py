from universe import character
from universe.character import display_character
from utils.input_utils import ask_choice, load_file
from universe.house import assign_house


def meet_friends(character):
    """
        The player boards the Hogwarts Express and meets Ron, Hermione, and Draco.
        Each interaction affects the character's attributes.
        :param character: dict
        :return: None
        """
    print("=" * 80)
    print("                            THE HOGWARTS EXPRESS")
    print("=" * 80)
    print()

    print("Hagrid drops you off at King's Cross Station with a warm pat on the shoulder.")
    print()
    print('"Platform 9¾ is between platforms 9 and 10," he reminds you.')
    print('"Just walk straight at the barrier. Don\'t stop, don\'t be scared.')
    print('Best do it at a bit of a run if you are the nervous kind!", he laughs.')
    print()
    print("You take a deep breath, grip your trolley, and run straight at the solid barrier.")
    print("You brace for impact, but instead...")
    print()
    input("Press Enter to continue...")
    print()

    print("You emerge onto a bustling platform filled with students and families.")
    print("A magnificent scarlet steam engine waits, its sign reading: Hogwarts Express.")
    print()
    print("You board the train, find an empty compartment, and settle in.")

    pet = None
    for item in character["Inventory"]:
        if item in ["Owl", "Cat", "Rat", "Toad"]:
            pet = item

    if pet == "Owl":
        print("Your owl hoots softly from its cage, ruffling its feathers.")
    elif pet == "Cat":
        print("Your cat meows and paws at the carrier, eager to explore.")
    elif pet == "Rat":
        print("Your rat squeaks quietly, whiskers twitching with curiosity.")
    elif pet == "Toad":
        print("Your toad croaks contentedly from its tank.")

    print()
    input("Press Enter to continue...")
    print()

    # Player meets Rpon
    print("The compartment door slides open.")
    print()
    print("A red-haired boy with a smudge of dirt on his nose pokes his head in.")
    print("He looks friendly, if a bit nervous.")
    print()
    print('"Hi! I\'m Ron Weasley. Mind if I sit with you?"')

    print()
    choice_ron = ask_choice('How do you respond?',
                            ['"Sure, have a seat!"', '"Sorry, I prefer to travel alone."'])

    if choice_ron == '"Sure, have a seat!"':
        print()
        print('"Brilliant!" Ron grins, hauling his trunk inside.')
        print("He plops down across from you with a sigh of relief.")
        print('"This is my first year at Hogwarts. Well, technically.')
        print('All my brothers have been. I\'ve got a lot to live up to."')
        print()
        print("He pulls out a slightly squashed sandwich.")
        print('"Mum made corned beef. Again. Want some?"')
        print()
        print("Ron seems like the kind of person who'd have your back.")
        character["Attributes"]["Loyalty"] += 1

    else:
        print()
        print("Ron's smile falters.")
        print('"Oh. Right. Yeah, I get it."')
        print("He backs out awkwardly and closes the door.")
        print()
        print("Through the window, you see him wandering down the corridor alone.")
        print("You feel a small pang of guilt, but you wanted the space.")
        character["Attributes"]["Ambition"] += 1

    print()
    input("Press Enter to continue...")
    print()

    # Player meets Hermnione
    print("A few minutes later, the door slides open again.")
    print()
    print("A girl with bushy brown hair and very serious eyes peers in.")
    print("She's already wearing her Hogwarts robes.")
    print()
    print("She looks directly at you, while she says:")
    print('"Hello, I\'m Hermione Granger. Have you ever read \'A History of Magic\'?"')

    print()
    choice_hermione = ask_choice('How do you respond?',
                                 ['"Yes, I love learning new things!"', '"Uh… no, I prefer adventures over books."'])

    if choice_hermione == '"Yes, I love learning new things!"':
        print()
        print("Hermione beams.")
        print('"Really? That\'s wonderful! So few people appreciate')
        print('the importance of reading ahead."')
        print()
        print("She sits down, pulling out a book.")
        print('"We should study together sometime. I have a feeling')
        print('you\'re going to do very well at Hogwarts."')
        print()
        print("You feel your mind sharpening already in her presence.")
        character["Attributes"]["Intelligence"] += 1

    else:
        print()
        print("Hermione looks slightly disappointed but nods understandingly.")
        print('"Well, I suppose not everyone learns the same way.')
        print('Practical experience has its merits too."')
        print()
        print("She glances at your confident posture.")
        print('"You seem like the type who learns by doing. That takes courage."')
        print()
        print("She leaves to continue searching for intellectual friends.")
        character["Attributes"]["Courage"] += 1

    print()
    input("Press Enter to continue...")
    print()

    # Player meets Draco
    print("Just as you're settling in, the door slides open once more.")
    print()
    print("A pale boy with slicked-back blonde hair stands in the doorway,")
    print("flanked by two larger boys who look like bodyguards.")
    print()
    print("He surveys the compartment with a smirk, something calculating in his expression.")
    print("He says it like you should already know who he is:")
    print('"I\'m Draco Malfoy. It\'s best to choose your friends carefully from the start, don\'t you think?"')

    print()
    choice_draco = ask_choice('How do you respond?',
                              ["Shake his hand politely.", "Ignore him completely.", "Respond with arrogance."])

    if choice_draco == "Shake his hand politely.":
        print()
        print("You shake his hand. His grip is firm, almost territorial.")
        print()
        print('"Smart choice," Draco says with satisfaction.')
        print()
        print('"You know how to recognize... opportunity. We\'re going to')
        print('be great friends. I can already tell." he says as he sweeps out.')
        print()
        print("You're not sure if you trust him, but you understand ambition when you see it.")
        character["Attributes"]["Ambition"] += 1

    elif choice_draco == 'Ignore him completely.':
        print()
        print("You deliberately turn your head and look out the window.")
        print()
        print("Draco's smirk vanishes.")
        print('"Suit yourself," he says coldly, his face flushing.')
        print('"You\'ll regret that. You could\'ve had powerful friends.')
        print()
        print("You stood by your principles. That's what matters.")
        character["Attributes"]["Loyalty"] += 1

    else:
        print()
        print('"I choose my own friends," you say coolly.')
        print('"I don\'t need your permission."')
        print()
        print("Draco's eyes narrow dangerously.")
        print('"Oh, you\'re going to regret that," he hisses.')
        print('"Mark my words. You just made an enemy."')
        print()
        print("He storms out, his bodyguards trailing behind.")
        print()
        print("Standing up to bullies takes guts. You don't regret it.")
        character["Attributes"]["Courage"] += 1

    print()
    input("Press Enter to continue...")
    print()

    print("The train continues its journey northward.")
    print("Through the window, you watch the countryside blur past.")
    print()
    print("Somewhere ahead lies Hogwarts Castle, and your future.")
    print()
    print("The choices you've made already say a lot about who you are.")
    print()
    print(f"Your updated attributes: {character["Attributes"]}")
    print()
    input("Press Enter to continue...")
    print()


def welcome_message():
    """
    This function displays Professor Dumbledore's welcome speech to the students.
    """
    print()
    print("=" * 80)
    print("                            ARRIVAL AT HOGWARTS")
    print("=" * 80)
    print()

    print("The train slows to a stop at Hogsmeade Station.")
    print()
    print("You step onto the platform, and there's Hagrid, towering above the crowd.")
    print('"Firs\' years! Firs\' years over here!" he calls, waving a lantern.')
    print()
    print("You follow him down a narrow path through the darkness.")
    print()
    input("Press Enter to continue...")
    print()

    print("Then you see it.")
    print()
    print("Across the black lake, perched atop a high mountain,")
    print("sits Hogwarts Castle.")
    print()
    print("Its windows sparkle in the starry sky, towers reaching toward the heavens.")
    print("It's the most magnificent thing you've ever seen.")
    print()
    print('"No more \'an four to a boat!" Hagrid calls out.')
    print()
    print("You climb into a small boat, and it glides across the glassy water by itself.")
    print("Then up a flight of stone steps until you reach the castle's entrance.")
    print()
    print("The massive oak doors swing open.")
    print()
    input("Press Enter to continue...")
    print()

    print("=" * 80)
    print("                            THE GREAT HALL")
    print("=" * 80)
    print()

    print("You step into the Great Hall, and your breath catches.")
    print()
    print("Thousands of candles float in midair above four long tables")
    print("where the rest of the students sit.")
    print()
    print("The tables are laid with glittering golden plates and goblets.")
    print()
    print("At the top of the hall is another long table where the teachers sit,")
    print("and above it all, the ceiling shows the night sky—")
    print("stars twinkling, clouds drifting past.")
    print()
    print('"It\'s bewitched to look like the sky outside," you hear Hermione whisper.')
    print('"I read about it in Hogwarts: A History."')
    print()
    input("Press Enter to continue...")
    print()

    print("The first-years are led to the front of the hall.")
    print()
    print("An old wizard with a long silver beard and half-moon spectacles")
    print("rises from the center of the High Table.")
    print()
    print("The hall falls silent.")
    print()
    print("His eyes twinkle with warmth as he surveys the students.")
    print()
    input("Press Enter to continue...")
    print()

    print("-" * 80)
    print()
    print("Professor Albus Dumbledore spreads his arms wide.")
    print()
    print('"Welcome to a new year at Hogwarts!"')
    print()
    print('"Before we begin our banquet, I would like to say a few words.')
    print('And here they are: Nitwit! Blubber! Oddment! Tweak!"')
    print()
    print('"Thank you!"')
    print()
    print("-" * 80)
    print()
    input("Press Enter to continue...")
    print()

    print("He sits back down.")
    print("You're not sure if he's joking or completely mad.")
    print("Around you, the older students are applauding and laughing.")
    print()
    print("Another teacher with a tall pointed hat and stern expression,")
    print("Professor McGonagall, steps forward")
    print("carrying an ancient, patched wizard's hat.")
    print()
    print("The Sorting Hat.")
    print()
    print("Your heart begins to race.")
    print("It's time.")
    print()
    input("Press Enter to continue...")
    print()


def sorting_ceremony(character):
    """
    This function conducts the Sorting Hat ceremony to assign the player to a house.
    """
    print()
    print("=" * 80)
    print("                            The Sorting Ceremony")
    print("=" * 80)
    print()

    print("Suddenly, a rip near the brim opens like a mouth, and the Hat begins to sing:")
    print()
    print('"Put me on and I will tell you')
    print('Where you ought to be.')
    print()
    print('You might belong in Gryffindor,')
    print('Where dwell the brave at heart,')
    print()
    print('Or yet in wise old Ravenclaw,')
    print('If you\'ve a ready mind,')
    print()
    print('Or perhaps in Slytherin')
    print('You\'ll make your real friends,')
    print()
    print('Or loyal Hufflepuff,')
    print('Where they are just and true!"')
    print("-" * 80)
    print()
    input("Press Enter to continue...")
    print()

    print("The Great Hall erupts in applause.")
    print()
    print("Professor McGonagall begins calling names alphabetically.")
    print()
    print("One by one, students approach the stool, have the Hat placed on their heads,")
    print("and after a moment, the Hat shouts out a house.")
    print()
    print("Finally, you hear your name called:")
    print()
    print(f'"{character["Last Name"]} {character["First Name"]}!"')
    print()
    input("Press Enter to continue...")
    print()

    print("Your legs feel like jelly as you walk to the front of the hall.")
    print("Every eye is on you. The silence is deafening.")
    print()
    print("You sit on the stool, and Professor McGonagall")
    print("lowers the Sorting Hat onto your head.")
    print("It's too large and falls over your eyes, plunging you into darkness...")
    print()
    input("Press Enter to continue...")
    print()

    print("-" * 80)
    print()
    print("A small voice speaks in your ear: the Hat's voice:")
    print()
    print('"Hmm... interesting. Very interesting indeed."')
    print('"I can see your qualities clearly..."')
    print()
    print('"But to truly know your heart, I must ask you some questions.')
    print('Answer honestly! I\'ll know if you don\'t!"')
    print()
    print("-" * 80)
    print()
    input("Press Enter to continue...")
    print()

    assigned_house = assign_house(character,
                                  [
                                      (
                                          "You see a friend in danger. What do you do?",
                                          ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
                                          ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
                                      ),
                                      (
                                          "Which trait describes you best?",
                                          ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking",
                                           "Intelligent and curious"],
                                          ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
                                      ),
                                      (
                                          "When faced with a difficult challenge, you...",
                                          ["Charge in without hesitation", "Look for the best strategy",
                                           "Rely on your friends", "Analyze the problem"],
                                          ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
                                      )
                                  ])

    print()
    print("-" * 80)
    print()
    print("The Hat contemplates for a moment...")
    print('"It\'s clear where you belong..."')
    print()
    input("Press Enter to continue...")
    print()

    print("The Hat takes a deep breath and shouts for all to hear:")
    print()
    print(f'"{assigned_house}!!!"')
    print()
    print("-" * 80)
    print()
    input("Press Enter to continue...")
    print()

    character["House"] = assigned_house

    print("You pull off the Hat and walk toward your new house table.")
    print()

    # House specific interaction
    if assigned_house == "Gryffindor":
        print("The Gryffindor table explodes with cheers!")
        print("Students in red and gold robes stand and applaud as you approach.")
        print()
        print("You sit down, and a prefect claps you on the back.")
        print('"Welcome to Gryffindor, house of the brave!"')

    elif assigned_house == "Slytherin":
        print("The Slytherin table erupts in applause, though it's more measured,")
        print("more calculating than the others.")
        print("Students in green and silver robes watch you with approval.")
        print()
        print("You sit down, and a prefect nods at you with respect.")
        print('"Welcome to Slytherin, house of the ambitious and cunning.')
        print('You\'ll go far here."')

    elif assigned_house == "Hufflepuff":
        print("The Hufflepuff table cheers warmly, every single student clapping.")
        print("Students in yellow and black robes beam at you with genuine welcome.")
        print()
        print("You sit down, and several students immediately introduce themselves.")
        print('"Welcome to Hufflepuff, house of the loyal and true!')
        print('You\'re going to love it here!"')

    elif assigned_house == "Ravenclaw":
        print("The Ravenclaw table applauds enthusiastically.")
        print("Students in blue and bronze robes nod at you with interest.")
        print()
        print("You sit down, and a prefect smiles at you.")
        print('"Welcome to Ravenclaw, house of the wise and clever.')
        print('We value wit and learning above all."')

    print()
    print(f"You've joined the noble house of {assigned_house}!")
    print()
    input("Press Enter to continue...")
    print()


def enter_common_room(character):
    """
    In this function, the player enters their house common room and receives a welcome speech.
    """
    print()
    print("=" * 80)
    print("                                Your new home")
    print("=" * 80)
    print()

    print("After the feast, the prefects lead the first-years out of the Great Hall.")
    print("You follow them through corridors, up staircases, down passages.")
    print()
    input("Press Enter to continue...")
    print()

    # KLoad data
    houses_data = load_file("data/houses.json")
    player_house = character["House"]
    house_info = houses_data[player_house]

    print(f"Finally, you arrive at the {player_house} common room entrance.")
    print()

    # House-specific entrance descriptions
    if player_house == "Gryffindor":
        print("You stop in front of a large portrait of a fat lady in a pink silk dress.")
        print()
        print('"Password?" she asks.')
        print('The prefect whispers: "Caput Draconis."')
        print()
        print("The portrait swings forward like a door, revealing a round opening.")

    elif player_house == "Slytherin":
        print("You descend deeper into the dungeons, where it's colder and darker.")
        print()
        print("The prefect stops at a bare stretch of stone wall and speaks:")
        print('"Pure-blood."')
        print()
        print("The wall slides aside, revealing a hidden entrance.")

    elif player_house == "Hufflepuff":
        print("You arrive at a pile of large barrels in a shadowy alcove.")
        print()
        print("The prefect taps a specific barrel in rhythm:")
        print("Tap-tap. Tap-tap-tap.")
        print()
        print("The lid swings open, revealing a passage.")

    elif player_house == "Ravenclaw":
        print("You climb a spiral staircase to a door with a bronze knocker")
        print("shaped like an eagle.")
        print()
        print('It speaks: "Which came first, the phoenix or the flame?"')
        print('The prefect answers: "A circle has no beginning."')
        print()
        print("The door swings open, satisfied with the answer.")

    print()
    input("Press Enter to continue...")
    print()

    print(f"     {house_info["emoji"]} " + "=" * 36 + f" {house_info['emoji']}")
    print()
    print(house_info["description"])
    print()
    print(house_info["installation_message"])
    print(f"The colors your house features are {', '.join(house_info['colors'])}.")
    print()
    print(f"     {house_info["emoji"]} " + "=" * 36 + f" {house_info['emoji']}")

    print()
    input("Press Enter to continue...")
    print()

    # Apply bonus attributes
    print("As you settle into your new house, you feel your qualities strengthening...")
    print()
    for attribute, bonus in house_info['bonus_attributs'].items():
        if attribute in character["Attributes"]:
            character["Attributes"][attribute] += bonus
            print(f"Your {attribute} increases by {bonus}!")

    print()
    input("Press Enter to continue...")
    print()

def start_chapter_2(char):
    print("~"*80)
    print("=" * 80)
    print("                Chapter II: Friends, Foes, and the Sorting Hat")
    print("=" * 80)
    print("~"*80)
    print()

    meet_friends(char)
    welcome_message()
    sorting_ceremony(char)
    enter_common_room(char)

    print()
    print("=" * 80)
    print("                                 Your Profile")
    print("." * 80)
    display_character(char)
    print("=" * 80)

    print()
    input("Press Enter to continue...")
    print()

    print("=" * 80)
    print()

    print("End of Chapter II!")
    print()
    print("On you way to Hogwarts, you met unforgettable friends.")
    print("You explored the vast, bustling castle and were assigned")
    print("to the house that suits you best, a place where your journey truly begins.")
    print()
    print("Take a deep breath ; your magical classes await!")

    print()
    input("Press Enter to continue...")
    print()

    return(char)