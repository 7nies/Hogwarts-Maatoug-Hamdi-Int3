from utils.input_utils import ask_number


def update_house_points(houses, house_name, points):
    if house_name in houses:
        houses[house_name] += points
        print(f"{points} for {house_name} ! Adding it up to {points} points.")
    else:
        print("House not found.")
    return houses

def display_winning_house(houses):
    max_point = 0
    winning_house = []
    for house in houses:
        if houses[house] > max_point:
            max_point = houses[house]
    for house in houses:
        if houses[house] == max_point:
            winning_house.append(house)
    if len(winning_house) == 1:
        print(f"The winning house is: {winning_house[0]} with {max_point} points!")
    else:
        print(f"It's a tie between: {', '.join(winning_house)} with {max_point} points each!")


def assign_house(character, questions):
    house_scores = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }
    house_scores["Gryffindor"] += 2 * character["Attributes"]["Courage"]
    house_scores["Slytherin"] += 2 * character["Attributes"]["Ambition"]
    house_scores["Hufflepuff"] += 2 * character["Attributes"]["Loyalty"]
    house_scores["Ravenclaw"] += 2 * character["Attributes"]["Intelligence"]
    for question_text, choices, houses in questions:
        print(question_text)
        for i in range(len(choices)):
            print(f"{i+1}. {choices[i]}")
        choice_num = ask_number("Your choice: ", 0, len(choices))
        chosen_house = houses[choice_num]
        house_scores[chosen_house] += 3
    print("\nSummary of scores:")
    for house, score in house_scores.items():
        print(f"{house}: {score} points")
    winning_house = max(house_scores, key=house_scores.get)
    return winning_house
