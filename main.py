from catmon import Catmon
from config import CATMON_TEMPLATES

print("Welcome to the world of catmon!")

catmon_is_picked: bool = False
player_catmon_choice: str = ""
enemy_catmon_choice: str = ""

while not catmon_is_picked:
    print("Choose a catmon:")
    player_catmon_choice = (input("mugi, buwie, raffy\n")).lower()
    print(f"You've selected {player_catmon_choice}!")
    if player_catmon_choice == "mugi":
        print(f"{player_catmon_choice} is a fire type catmon that will fuck you up")
        enemy_catmon_choice = "buwie"
        catmon_is_picked = True
    elif player_catmon_choice == "buwie":
        print(
            f"{player_catmon_choice} is a water type catmon that will give u wet kisses"
        )
        enemy_catmon_choice = "raffy"
        catmon_is_picked = True
    elif player_catmon_choice == "raffy":
        print(
            f"{player_catmon_choice} is a grass type catmon that will ask u to touch some grass"
        )
        enemy_catmon_choice = "mugi"
        catmon_is_picked = True
    else:
        print("That catmon isn't in the choices!")

# mypy does not like unpacking
player_catmon: Catmon = Catmon(**CATMON_TEMPLATES[player_catmon_choice])  # type: ignore

nickname_is_given: bool = False

while not nickname_is_given:
    if_give_nickname_input: str = (
        input(f"\nWould you like to give your {player_catmon.name} a nickname? Y/N")
    ).lower()

    if if_give_nickname_input == "y":
        player_catmon_nickname_input: str = input("Enter nickname: ")
        player_catmon.nickname = player_catmon_nickname_input
        nickname_is_given = True
    elif if_give_nickname_input == "n":
        nickname_is_given = True
    else:
        print("That's not a valid input!")
        nickname_is_given = False

print("Let's have our first battle!")

# mypy does not like unpacking
enemy_catmon: Catmon = Catmon(**CATMON_TEMPLATES[enemy_catmon_choice])  # type: ignore

print(f"Your Catmon: {player_catmon.nickname} vs Enemy Catmon: {enemy_catmon.nickname}")
