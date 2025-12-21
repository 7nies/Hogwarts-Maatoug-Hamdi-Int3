from universe.character import add_item
from universe.house import update_house_points, display_winning_house
from utils.input_utils import load_file, ask_choice, ask_number, ask_text
import random

def learn_spells(character, file_path):
    """
    In this function, the player learns 5 spells during their first magic lessons.
    :param character: dict
    :param file_path: str
    """

    print()
    print("=" * 80)
    print("                              First magic lessons")
    print("=" * 80)
    print()

    print()
    print("You already attend your first classes:")
    print("Transfiguration with Professor McGonagall,")
    print("Potions in the dungeons with Professor Snape,")
    print("Charms with tiny Professor Flitwick,")
    print("Defence against the Dark Arts with Professor Umbridge...")
    print()
    print("...But today is special. Today, you learn your first real spells.")
    print()
    input("Press Enter to continue...")
    print()

    spells_list = load_file(file_path)

    print("Professor Flitwick stands before the class, his wand raised.")
    print()
    print('"Magic," he squeaks in his high voice, "is not just about waving')
    print('a stick and saying funny words. It requires focus, intent, and practice!"')
    print()
    print("He demonstrates a spell, and feathers begin floating around the room.")
    print()
    print('"Now, you will each learn five fundamental spells.')
    print('One offensive, one defensive, and three utility spells."')
    print()
    input("Press Enter to continue...")
    print()

    learned_spells = []
    offensive = []
    defensive = []
    utility = []

    while len(learned_spells) < 5:
        spell = random.choice(spells_list)
        if spell not in learned_spells:
            if spell["type"] == "Offensive" and len(offensive) < 1:
                offensive.append(spell)
            elif spell["type"] == "Defensive" and len(defensive) < 1:
                defensive.append(spell)
            elif spell["type"] == "Utility" and len(utility) < 3:
                utility.append(spell)
        learned_spells.append(spell)

    print("Over the next few hours, you practice diligently...")
    print()

    for spell in learned_spells:
        add_item(character, "Spells", spell["name"])

        if spell["type"] == "Offensive":
            print(f"⚔  Professor Flitwick teaches you: {spell['name']}")
            print(f'   "{spell["description"]}"')

        elif spell["type"] == "Defensive":
            print(f"🛡  Professor Flitwick teaches you: {spell['name']}")
            print(f'   "{spell["description"]}"')

        else:
            print(f"✴  Professor Flitwick teaches you: {spell['name']}")
            print(f'   "{spell["description"]}"')

        print()
        input("Press Enter to continue...")
        print()

    print("=" * 80)
    print()
    print("Hours later, you lower your wand, exhausted but exhilarated.")
    print()
    print("Professor Flitwick saw you.")
    print('"Excellent work! You\'re a natural!"')
    print()

    print("You have completed your basic spell training at Hogwarts!")
    print()
    print("=" * 80)
    print()
    print("Here are the spells you now master:")
    print()
    for spell in learned_spells:
        print(f"  • {spell['name']} ({spell['type']})")
        print(f"    {spell['description']}")
        print()

    input("Press Enter to continue...")
    print()

def magic_quiz(character, file_path):
    """
    This function offers an interactive quiz with 4 random questions to test the player's knowledge
    :param character: dict
    :param file_path: str
    :return: int
    """
    print()
    print("=" * 80)
    print("                       Professor Snape's surprise test")
    print("=" * 80)
    print()

    print("The next day, you enter the Potions classroom in the dungeons.")
    print("It's cold and dimly lit. Pickled creatures float in jars along the walls.")
    print()
    print("Professor Snape sweeps into the room, his black robes billowing behind him.")
    print("He surveys the class with cold, dark eyes.")
    print()
    input("Press Enter to continue...")
    print()

    print('"Today," he says in a soft, menacing voice, "we will test')
    print('whether or not you\'ve been paying attention in your classes..."')
    print()
    print("He waves his wand, and questions appear on the blackboard.")
    print()
    print('"Four questions. Answer correctly, and your house gains points.')
    print('Fail... and you may wish you had studied harder."')
    print()
    print("Your heart pounds as you read the first question.")
    print()
    input("Press Enter to continue...")
    print()

    quiz = load_file(file_path)
    questions = []
    score = 0
    player_house = character["House"]

    while len(questions) < 4:
        q = random.choice(quiz)
        if q not in questions:
            questions.append(q)

    question_num = 1
    for q in questions:
        print("-" * 80)
        print()
        print(f"Question {question_num}/4:")
        print()
        print(f"{q['question']}")
        print()
        user_answer = ask_text("Your answer: ")
        print()

        if user_answer == q["answer"]:
            print("✓ Correct!")
            print()
            print("Professor Snape gives the slightest nod.")
            print(f'"Acceptable. +25 points for {player_house}."')
            print()
            score += 25
        else:
            print("✗ Incorrect.")
            print()
            print(f'Snape\'s lip curls. "Wrong. The answer was: {q["answer"]}"')
            print("He moves on without another word.")
            print()

        question_num += 1
        input("Press Enter to continue...")
        print()

    print("=" * 80)
    print()
    if score == 100:
        print("Professor Snape looks almost... impressed.")
        print('"Perfect score. Remarkable."')
    elif score >= 50:
        print("Professor Snape nods curtly.")
        print('"Passable."')
    else:
        print("Professor Snape sneers.")
        print('"Disappointing. I expected nothing less."')

    print()
    print(f"Final score: {score} points earned for {player_house}!")
    print()
    print("=" * 80)
    print()
    input("Press Enter to continue...")
    print()

    return score


def start_chapter_3(character, houses):
    """
    This function orchestrates chap3.
    :param character: dict
    :param houses: dict
    """
    print()
    print("~" * 80)
    print("=" * 80)
    print("                    Chapter III: Wand, words, and wonders")
    print("=" * 80)
    print("~" * 80)
    print()

    print("The first weeks at Hogwarts fly by in a blur of new experiences.")
    print("A month has passed since the Sorting Ceremony.")
    print()
    print("Hogwarts has become a maze of discovery...")
    print("...secret passages behind tapestries,")
    print("ghosts drifting through walls,")
    print("portraits that gossip and argue,")
    print("and staircases that change destination on a whim.")
    print()
    input("Press Enter to continue...")
    print()

    print("You've settled into a routine:")
    print("Breakfast in the Great Hall as owls deliver the morning post.")
    print("Classes scattered throughout the castle,")
    print("some fascinating, some... less so.")
    print("Homework by candlelight in the common room.")
    print("And always, always, the thrill of learning real magic.")
    print()
    input("Press Enter to continue...")
    print()

    learn_spells(character, "data/spells.json")
    quiz_score = magic_quiz(character, "data/magic_quiz.json")
    player_house = character["House"]
    update_house_points(houses, player_house, quiz_score)

    print()
    print("=" * 80)
    print("                             Houses Leaderboard")
    print("=" * 80)
    print()

    display_winning_house(houses)

    print()
    input("Press Enter to continue...")
    print()

    print("=" * 80)
    print()

    print("End of Chapter III!")
    print()
    print("Today, you leave the dungeons feeling accomplished.")
    print("You proved yourself in the classrooms.")
    print("You've learned powerful magic and earned points for your house.")
    print("But you can't shake the feeling that greater challenges lie ahead...")
    print()
    input("Press Enter to continue...")
    print()




