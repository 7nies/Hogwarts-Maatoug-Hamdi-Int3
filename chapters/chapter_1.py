from universe.character import *
from universe.house import *
from utils.input_utils import *

# METTRE DES ESPACES (du type print() pour sauter des lignes) DANS L'ECRITURE sinon c trop compact
# aussi ne pas faire des lignes trop longues stp
# tu penses quoi du texte sinon???
# jsp si on a le droit de mettre la letter avant la character creation

def introduction():
    """
    This function displays the introduction for chapter 1, including the ascii art.
    """
    hogwarts_ascii = """





                                  #.                                                                 
                                .# #.                                                                
                               ##   #                     #        #+   ##                           
                              ##     #                     +.    ###    +                ##          
                             #+       #                   ### +####                                  
          #                 ##         #                  ### #+#######                              
         ###  #           .#            #                   ##########.           ++     #           
         # #. ##         ##              #                  #######               #. +##     +       
        #-  ## .#       ##                #               +##   ###               ## ## .   +##.     
       ##        #     ####              ###                     ##   #         .    +###            
       #          #       #-   -#   ##   ##                       #  +###       ###. #   #-          
      ##   #       #      ##   -#   ##   ##                            #             ###             
     -#    #     ####     ###            ##                                          + ##            
     #          ###   .  #####           ##  #+  #-                                     ##           
    ####+        ###########             .##########                          ####       ##          
        ##                                                                     ###        ##         
        ###      ###   ###                                    #.++  ##                    .##        
        ###      ###   ###          -####+            +####   #####+###                     ##       
        #        ###   ###   .##   ##- ##+  ##     ##  +  #+  ##    ##    ##                ###      
        #        ###   ####### ##- ##  ##+  ##  #  ##   . ##  ##    ##  ##  #                ###     
        #      # ###  -### +##  ## ##  +#+  ##  #  ## ### ##  ##    ##   ###                  ###    
        #        ####  ### -##  ## ## .##+  ## ##  #   ##+##  ##    ##    -##                  #     
        #        ###   ###  ##  ##   # +#+   ##  ##    .  .         ##  +####                        
       +#        ###.  ###    +        ##+                          ##    #                          
       ##        ###+  ###          #  ##                                                            
       ##             +###         ## #                                                              
       ##                           #                                                                
       ##                                                                                            
     +                                                                                               



"""

    print(hogwarts_ascii)

    print()
    print("=" * 80)
    print("                    Chapter I: Fall into the magical world")
    print("=" * 80)
    print()

    print("An ordinary child, living an ordinary life...")
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
    print()
    print("July 31st. Your birthday. Not that anyone here cares.")
    print("You're lying in your cupboard, listening to Dudley snoring upstairs, when you hear it.")
    print()
    print("Tap. Tap. Tap.")
    print()
    print("Something is pecking at the window.")
    input("Press Enter to continue...")


def create_character():
    """
    This function aims to regroup the necessary information to the character creation through multiple scenarios (owl for the name, magic crystal for attributes).
    :return: dict
    """
    print()
    print("=" * 80)
    print("                        The letter arrives...")
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
    print("You glance toward the stairs—everyone's asleep. You carefully open the window.")
    print()
    print("The owl swoops in silently and drops the letter into your hands.")
    print("It's surprisingly heavy, sealed with purple wax bearing a coat of arms:")
    print("a lion, an eagle, a badger, and a serpent surrounding a large letter 'H'.")
    print()
    input("Press Enter to continue...")
    print()

    print("Before you can break the seal, the owl gives a sharp hoot.")
    print("Its eyes begin to glow with a soft golden light.")
    print("This stare only makes you understand the owl's instructions.")
    print()
    print("You state your full name, truthfully and clearly.")
    print("You can feel that the magic will know if you lie.")
    print()
    print("The letter grows warm in your hands, waiting.")
    print()
    last_name = ask_text("Affirm your last name:   ")
    first_name = ask_text("Affirm your first name:   ")
    print()
    print("The moment you speak your name, the wax seal glows brightly and melts away.")
    print("The owl hoots approvingly and flies back out into the night.")
    print()
    input("Press Enter to continue...")
    print()

    print("Suddenly, something small and crystalline falls out of the envelope.")
    print()
    print("It's a perfectly smooth crystal, no bigger than a marble, that shifts through colors—red, blue, yellow, green...")
    print("...like a tiny rainbow trapped in glass.")
    print()
    input("Press Enter to continue...")
    print()

    print("You place the crystal in your palm. It immediately begins to pulse with light.")
    print()
    print("=" * 80)
    print("                           The Prism of Truth")
    print("=" * 80)
    print()
    print("The crystal's voice echoes in your mind...:")
    print()
    print('I can see who you truly are.')
    print('Answer honestly, for I will measure the four qualities')
    print('that define every witch and wizard:')
    print('courage, intelligence, loyalty and ambition."')
    print()
    print("You must answer with a number between 1 and 10.")
    print()
    input("Press Enter to continue...")
    print()

    print("The crystal glows RED, warm like courage itself...")
    courage = ask_number('"How brave are you when facing the unknown?" ', 1, 10)
    print()

    print("The crystal shifts to BLUE, cool like a vast library...")
    intelligence = ask_number('"How sharp is your mind? How deep is your thirst for knowledge?" ', 1,10)
    print()

    print("The crystal turns YELLOW, steady like the sun...")
    loyalty = ask_number('"How loyal are you to those you care about?" ',1,10)
    print()

    print("The crystal gleams GREEN, bright like ambition's fire...")
    ambition = ask_number('"How determined are you to achieve your goals and prove your worth?" ', 1,10)
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
    print("                           Your Profile")
    print("=" * 80)
    print(display_character(character))
    print()
    print("=" * 80)
    print()
    input("Press Enter to continue...")
    print()


def receive_letter():
    """
    This function simulates the player's reading of the Hogwarts invitation letter, issuing in either a refusal or the acceptance.
    """

    print("You can hear the blood rushing through your veins.")
    print()
    print("Your eyes go back to the letter on the floor.")
    print("You unfold the letter with trembling hands:")
    print()
    print("-" * 80)
    print("                             HOGWARTS SCHOOL")
    print("                        of WITCHCRAFT and WIZARDRY")
    print()
    print(f"Dear Future Student,")
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
        print()
        print('"Yes," you whisper to the empty room. "Yes, I\'m going to Hogwarts."')
        print()
        print("The letter glows warmly, as if approving your choice.")
        print()
        input("Press Enter to continue...")
        print()

    print("You hide the letter under your thin mattress, mind racing.")
    print("How will you get to this school? Where even IS Hogwarts?")
    print()
    print("As if an answer, you hear it:")
    print()
    print("*BOOM BOOM BOOM*")
    print()
    print("Someone is pounding on the front door.")
    print()
    input("Press Enter to continue...")
    print()

def meet_hagrid():
    print("-" * 80)
    print("                        The Keeper of Keys")
