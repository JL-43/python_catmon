from typing import List

from logs import Logs

logs = Logs()


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
        logs.log_battle(f"{self.name} attacks {other.name} for {damage_taken} damage")

    def take_damage(self, damage_taken: int):
        self.health -= damage_taken

    def heal(self, heal_amount: int):
        if (self.health + heal_amount) > self.max_health:
            # get the difference between current health to max health (health_to_full)
            # set the current health to maximum health
            # use the health_to_full computed value for the amount healed for the logs

            health_to_full = self.max_health - self.health
            self.health = self.max_health
            logs.log_battle(f"{self.name} heals for {health_to_full}")
        else:
            self.health += heal_amount
            logs.log_battle(f"{self.name} heals for {heal_amount}")

    def display_stats(self):
        for attribute, value in vars(self).items():
            print(f"{attribute}: {value}")

    def display_moves(self):
        print("Moves:")
        for move in self.moves:
            print(f"  - {move}")
