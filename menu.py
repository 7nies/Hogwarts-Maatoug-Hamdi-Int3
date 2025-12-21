from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import start_chapter_2
from chapters.chapter_3 import start_chapter_3
from utils.input_utils import ask_choice


def display_main_menu():
    """
    This function displays the main menu and gets player choice.
    :return: str
    """
    choice = ask_choice("Do you want to start your adventure?   ",
               ["Yes", "No, exit the game"])
    return choice

def launch_menu_choice():
    """
    Controls the main menu loop and orchestrates the game's progression.
    :return:
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
            #        ###   ###   .##   ##- ##+  ##     ##     #+  ##    ##    ##                ###      
            #        ###   ####### ##- ##  ##+  ##  #  ##  .+ ##  ##    ##  ##  #                ###     
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
    choice = display_main_menu()
    if choice == "Yes":
        print()
        print("Your magical journey begins...")
        print()
        input("Press Enter to continue...")
        print()

        houses = {
            "Gryffindor": 0,
            "Slytherin": 0,
            "Hufflepuff": 0,
            "Ravenclaw": 0
        }

        char = start_chapter_1()
        char = start_chapter_2(char)
        start_chapter_3(char, houses)

        # Texte de fin
        print()
        print("=" * 80)
        print("              Thank you for playing! :3")
        print("                     This game has been made by Ines Maatoug and Anas Hamdi ^_^")
        print("=" * 80)
        print()

    else:
        print()
        print("Perhaps another time, then.")
        print()
        print("The magical world will be waiting when you're ready...")
        print()
        exit()
