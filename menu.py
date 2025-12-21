from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import start_chapter_2
from utils.input_utils import ask_choice

def launch_menu_choice():
    choice = ask_choice(
        "Do you want to start your adventure?   ",
        ["Yes", "No"]
    )

    if choice == "Yes":
        char = start_chapter_1()
        start_chapter_2(char)