class Catmon:

    """
    Attributes
    Name: The name of the Catmon.
    Type: The type of the Catmon (e.g., Water, Fire, Grass).
    Health: The current health of the Catmon.
    Max Health: The maximum health of the Catmon.
    Level: The level of the Catmon.
    Moves: A collection of moves or attacks that the Catmon can perform.

    Methods
    Attack: Allows the Catmon to perform an attack on another Catmon.
    Take Damage: Reduces the Catmon's health when attacked.
    Heal: Restores the Catmon's health (optional).
    Display Stats: Prints or returns the Catmon's current stats."""

    def __init__(self, name, type, health, max_health, moves, level=1):
        self.name = name
        self.type = type
        self.health = health
        self.max_health = max_health
        self.moves = moves  # This could be a dictionary or array
        self.level = level

    def attack(self, other):
        other.health -= 5

    def take_damage(self):
        self.health -= 5

    def heal(self):
        self.health += 10

    def display_stats(self):
        for attribute, value in vars(self).items():
            print(f"{attribute}: {value}")


mugi = Catmon("mugi", "fire", 100, 100, ["tackle", "heal"])
buwie = Catmon("buwie", "water", 100, 100, ["tackle", "heal"])

print("----")
mugi.display_stats()
print("----")
buwie.display_stats()

print("----")
print("mugi attacks buwie")
mugi.attack(buwie)

print("----")
mugi.display_stats()
print("----")
buwie.display_stats()
