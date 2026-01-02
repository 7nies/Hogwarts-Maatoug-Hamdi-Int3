from universe.character import display_character
from universe.house import update_house_points, display_winning_house
from utils.input_utils import load_file
import random

def create_team(house, team_data, is_player, player):
    """
    Creates team dict for Quidditch match.
    :param house: str
    :param team_data: str
    :param is_player: bool
    :param player: dict
    :return: dict
    """
    house_data = load_file(team_data)
    team = {
        "name": house,
        "score": 0,
        "goals_scored": 0,
        "goals_blocked": 0,
        "caught_snitch": False,
        "players": []
    }
    house_players = house_data[house]["players"]
    if is_player and player:
        seeker_name = f"{player['First Name']} {player['Last Name']} (Seeker)"
        team["players"].append(seeker_name)
        for p in house_players[1:]:
            team["players"].append(p)
    else:
        team["players"] = house_players
    return team

def attempt_goal(attacking_team, defending_team, player_is_seeker):
    """
    Simulates an attempt to score a goal.
    :param attacking_team: dict
    :param defending_team: dict
    :param player_is_seeker: bool
    """
    chance_goal = random.randint(1, 10)
    if chance_goal >= 6:
        if player_is_seeker:
            scorer = attacking_team["players"][0]
        else:
            scorer = random.choice(attacking_team["players"])
        attacking_team["score"] += 10
        attacking_team["goals_scored"] += 1
        print(f"{scorer} scores a goal for {attacking_team['name']}! (+10 points)")
    else:
        defending_team["goals_blocked"] += 1
        print(f"{defending_team['name']} blocks the attack!")

def golden_snitch_appears():
    """
        Randomly determines if the Golden Snitch appears.
    :return: bool
    """
    snitch_appears = False
    chance_snitch = random.randint(1, 6)
    if chance_snitch == 6:
        snitch_appears = True
    return snitch_appears

def catch_golden_snitch(e1, e2):
    """
    Randomly determines which team catches the Golden Snitch.
    :param e1: dict
    :param e2: dict
    :return: dict
    """
    winning_team = random.choice([e1, e2])
    winning_team["score"] += 150
    winning_team["caught_snitch"] = True
    return winning_team

def display_score(e1, e2):
    """
    Displays the current score of both teams
    :param e1: dict
    :param e2: dict
    """
    print("Current score:")
    print(f"→ {e1['name']}: {e1['score']} points")
    print(f"→ {e2['name']}: {e2['score']} points")

def display_team(house, team):
    """
    Displays the team name and players
    :param house: str
    :param team: dict
    """
    print(f"\n{house} Team:")
    for player in team["players"]:
        print(f"- {player}")


def quidditch_match(character, houses):
    """
    Manages the entire Quidditch match between player's house and opponent's.
    :param character: dict - player character
    :param houses: dict - house points dictionary
    """
    print()
    print("=" * 80)
    print("                             The Quidditch match")
    print("=" * 80)
    print()

    print("The day of the match has arrived.")
    print()
    print("You tighten your grip on your broomstick.")
    print("Your heart thrums in rhythm with the pulse of the pitch.")
    print("Banners wave in the wind, students cheer, and excitement fills the air.")
    print()
    input("Press Enter to continue...")
    print()

    teams_data = load_file("data/teams_quidditch.json")
    player_house = character["House"]
    available_houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    available_houses.remove(player_house)
    opponent_house = random.choice(available_houses)

    print(f"Today's match: {player_house} vs {opponent_house}!")
    print()
    input("Press Enter to continue...")
    print()

    player_team = create_team(player_house, "data/teams_quidditch.json", is_player=True, player=character)
    opponent_team = create_team(opponent_house, "data/teams_quidditch.json", is_player=False, player=None)
    display_team(player_house, player_team)
    display_team(opponent_house, opponent_team)
    print()

    print(f"You are playing for {player_house} as the Seeker!")
    print("Your job: catch the Golden Snitch and win the match...")
    print()
    input("Press Enter to begin the match...")
    print()
    print("=" * 80)
    print("Madam Hooch’s whistle pierces the morning.")
    print("With a flick of her wand, the match begins.")
    print("")
    print("=" * 80)
    print()

    match_over = False
    turn = 1
    max_turns = 20

    while turn <= max_turns and not match_over:
        print(f"━━━ Turn {turn} ━━━")
        print()

        attempt_goal(player_team, opponent_team, player_is_seeker=True)
        attempt_goal(opponent_team, player_team, player_is_seeker=False)
        display_score(player_team, opponent_team)

        print()
        print("The scoreboard shimmers like enchanted numerals, reflecting every strike and block:")
        display_score(player_team, opponent_team)
        print()

        if golden_snitch_appears():
            print("A golden glint streaks across the sky! The Golden Snitch has appeared!")
            print("Both Seekers dive, slicing through wind like arrows of light.")
            print()
            input("Press Enter to continue...")
            print()

            snitch_catcher = catch_golden_snitch(player_team, opponent_team)
            print(f"The Golden Snitch has been caught by {snitch_catcher['name']}! +150 points!")
            print()
            match_over = True

        if not match_over:
            print("The match continues, a relentless ballet of courage, skill, and strategy.")
            print("You tilt and twist, eyes sharp for every shimmer of gold in the sky.")
            print()
            input("Press Enter to continue...")
            print()

        turn += 1
    print("Madam Hooch blows her whistle again, echoing across the stands.")
    print("The match ends. Cheers and applause fill the air as players descend from the sky.")
    print()
    print("=" * 80)
    print("                              End of match!")
    print("=" * 80)
    print()

    display_score(player_team, opponent_team)
    print()

    if player_team["score"] > opponent_team["score"]:
        winner = player_team
        print(f"Triumph! {player_team["name"]} emerges victorious!")
        print("Confetti swirls around your broom as your housemates lift you onto their shoulders.")
        print("The thrill of flight and battle lingers in the air.")
    elif opponent_team["score"] > player_team["score"]:
        winner = opponent_team
        print(f"{opponent_team["name"]} claims victory this day.")
        print("Though valiant, your team falls short.")
        print("Your teammates pat you on the back.")
        print('"We\'ll get them next time," they say.')
        print()
        print("Yet the thrill of flight and battle lingers.")
    else:
        winner = None
        print("The match ends in a tie...a rare and magical stalemate!")

    if winner:
        print("You feel it in your bones.")
        print()
        update_house_points(houses, winner["name"], 500)
        print(f"{winner['name']} earns additional glory: 500 points to their house!")
    print()
    input("Press Enter to continue...")
    print()

def start_chapter_4(character, houses):
    """
    Orchestrates Chapter 4: The Quidditch Match
    :param character: dict
    :param houses: dict
    """
    print("~" * 80)
    print("=" * 80)
    print("                Chapter IV: The Chase of the Golden Snitch")
    print("=" * 80)
    print("~" * 80)
    print()

    print("Months have unfurled like shifting pages")
    print("since you first arrived at Hogwarts.")
    print("The corridors hum with secrets,")
    print("the staircases twist in impossible ways,")
    print("and the portraits whisper of past glories.")
    print()
    print("You've mastered spells, brewed potions, and earned points for your house.")
    print("But today is different.")
    print()
    input("Press Enter to continue...")
    print()

    print("The castle seems to hold its breath.")
    print("In the crisp morning air, banners flutter above the Quidditch pitch,")
    print("each representing the pride and spirit of its house.")
    print("Something extraordinary is about to unfold.")
    print()
    print("Today, you face your greatest challenge yet.")
    print()
    input("Press Enter to continue...")
    print()

    print("Tryouts were intense. Competition was fierce.")
    print("But you made the team as Seeker: the key to victory.")
    print()
    print("You've trained with every sunrise, flying lap after lap around the pitch.")
    print("Your reflexes are sharp. Your eyes are keen.")
    print()
    print(f"Today, {character['House']} takes the field.")
    print()
    input("Press Enter to continue...")
    print()

    quidditch_match(character, houses)

    print("You return to the castle, exhausted but exhilarated.")
    print()
    print("The thrill of flying, the roar of the crowd, the rush of competition...")
    print("you'll never forget this day.")
    print()
    input("Press Enter to continue...")
    print()

    print("=" * 80)
    print("                             Final House standing")
    print("=" * 80)
    print()
    display_winning_house(houses)
    print()
    input("Press Enter to continue...")
    print()

    print("=" * 80)
    print("                                 Your Profile")
    print("." * 80)
    display_character(character)
    print("=" * 80)

    print()
    input("Press Enter to continue...")
    print()


    print("End of Chapter IV!")
    print()
    print("You soar through memory, feel the wind still on your face.")
    print("You proved yourself as Seeker. As champion. As a part of something greater.")
    print()
    print(f"{character['House']} will remember this day... You will too.")
    print("The story continues, as the magic never ends!")
    print()
    print("=" * 80)
    print()
    input("Press Enter to finish...")
    print()

    return character, houses