from catmon import Catmon

print("Welcome to the world of catmon!")

catmon_is_picked: bool = False

while not catmon_is_picked:
    print("Choose a catmon:")
    user_catmon_choice = input("Mugi, Buwie, Raffy\n")
    print(f"You've selected {user_catmon_choice}!")
    if user_catmon_choice == "Mugi":
        print(f"{user_catmon_choice} is a fire type catmon that will fuck you up")
        catmon_is_picked = True
    elif user_catmon_choice == "Buwie":
        print(
            f"{user_catmon_choice} is a water type catmon that will give u wet kisses"
        )
        catmon_is_picked = True
    elif user_catmon_choice == "Raffy":
        print(
            f"{user_catmon_choice} is a grass type catmon that will ask u to touch some grass"
        )
        catmon_is_picked = True
    else:
        print("That catmon isn't in the choices!")
