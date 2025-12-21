from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import start_chapter_2
from chapters.chapter_3 import start_chapter_3
from utils.input_utils import ask_choice

def launch_menu_choice():
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
    choice = ask_choice(
        "Do you want to start your adventure?   ",
        ["Yes", "No"]
    )

    if choice == "Yes":
        houses = {
            "Gryffindor": 0,
            "Slytherin": 0,
            "Hufflepuff": 0,
            "Ravenclaw": 0
        }
        char = start_chapter_1()
        char = start_chapter_2(char)
        start_chapter_3(char, houses)
