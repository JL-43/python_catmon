from typing import List


class Move:
    def __init__(self, name: str, power: int, type: str, category: str):
        self.name = name
        self.power = power
        self.type = type
        self.category = category

    def __str__(self):
        return f"Move: Name: {self.name}, Power: {self.power}, Type: {self.type}, Category: {self.category}"

    def __repr__(self):
        return f"Move: Name: {self.name}, Power: {self.power}, Type: {self.type}, Category: {self.category}"


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

    def __init__(
        self,
        name: str,
        type: str,
        health: int,
        max_health: int,
        moves: List[Move],
        level: int = 1,
    ):
        self.name = name
        self.type = type
        self.health = health
        self.max_health = max_health
        self.moves = moves  # This could be a dictionary or array
        self.level = level

    def use_move(self, other: "Catmon", selected_move: Move) -> None:
        if selected_move.category == "attack":  # attack move
            self.attack(other, selected_move.power)
        elif selected_move.category == "heal":  # heal move
            heal_amount = selected_move.power
            self.heal(heal_amount)

    def attack(self, other: "Catmon", damage_taken: int):
        other.take_damage(damage_taken)

    def take_damage(self, damage_taken: int):
        self.health -= damage_taken

    def heal(self, heal_amount: int):
        if (self.health + heal_amount) > self.max_health:
            self.health = self.max_health
        else:
            self.health += heal_amount

    def display_stats(self):
        for attribute, value in vars(self).items():
            print(f"{attribute}: {value}")

    def display_moves(self):
        print("Moves:")
        for move in self.moves:
            print(f"  - {move}")


tackle = Move("tackle", 5, "normal", "attack")
heal = Move("heal", 3, "normal", "heal")

mugi_moves = [tackle, heal]
buwie_moves = [tackle, heal]

mugi = Catmon("mugi", "fire", 100, 100, mugi_moves)
buwie = Catmon("buwie", "water", 100, 100, buwie_moves)

print("----")
mugi.display_stats()
print("----")
buwie.display_stats()

print("----")
print("mugi attacks buwie for 5")
mugi.use_move(buwie, tackle)

print("----")
mugi.display_stats()
print("----")
buwie.display_stats()

print("----")
print("buwie heals for 3")
buwie.use_move(mugi, heal)

print("----")
mugi.display_stats()
print("----")
buwie.display_stats()
