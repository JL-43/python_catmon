from catmon import Catmon
from config import CATMON_TEMPLATES

print("Welcome to the world of catmon!")

catmon_is_picked: bool = False
player_catmon_choice: str = ""

while not catmon_is_picked:
    print("Choose a catmon:")
    player_catmon_choice = (input("mugi, buwie, raffy\n")).lower()
    print(f"You've selected {player_catmon_choice}!")
    if player_catmon_choice == "mugi":
        print(f"{player_catmon_choice} is a fire type catmon that will fuck you up")
        catmon_is_picked = True
    elif player_catmon_choice == "buwie":
        print(
            f"{player_catmon_choice} is a water type catmon that will give u wet kisses"
        )
        catmon_is_picked = True
    elif player_catmon_choice == "raffy":
        print(
            f"{player_catmon_choice} is a grass type catmon that will ask u to touch some grass"
        )
        catmon_is_picked = True
    else:
        print("That catmon isn't in the choices!")

# mypy does not like unpacking
player_catmon: Catmon = Catmon(**CATMON_TEMPLATES[player_catmon_choice])  # type: ignore
player_catmon.display_stats()
player_catmon.display_moves()
