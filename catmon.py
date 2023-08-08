import logging
from typing import List

from logs import Logs

logs = Logs()

TYPE_EFFECTIVENESS = {
    "Fire": {
        "super_effective": ["Grass"],
        "not_effective": ["Water", "Fire"],
    },
    "Water": {
        "super_effective": ["Fire"],
        "not_effective": ["Water", "Grass"],
    },
    "Grass": {
        "super_effective": ["Water"],
        "not_effective": ["Fire", "Grass"],
    },
    "Normal": {},
}


class Move:
    def __init__(self, name: str, power: int, category: str, move_type: str):
        self.name = name
        self.power = power
        self.category = category
        self.move_type = move_type

    def __str__(self):
        return f"Move: Name: {self.name}, Power: {self.power}, Category: {self.category}, Type: {self.move_type}"

    def __repr__(self):
        return f"Move: Name: {self.name}, Power: {self.power}, Category: {self.category}, Type: {self.move_type}"


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
        atk: int,
        def_: int,
        sp_atk: int,
        sp_def: int,
        speed: int,
        level: int = 1,
    ):
        self.name = name
        self.type = type
        self.health = health
        self.max_health = max_health
        self.moves = moves
        self.atk = atk
        self.def_ = def_
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.level = level

    def use_move(self, other: "Catmon", selected_move: Move) -> None:
        if selected_move.category == "attack":  # attack move
            self.attack(
                other,
                selected_move.power,
                selected_move.category,
                selected_move.move_type,
            )
        elif selected_move.category == "heal":  # heal move
            heal_amount = selected_move.power
            self.heal(heal_amount)

    def attack(
        self, other: "Catmon", move_power: int, move_category: str, move_type: str
    ):
        # effectiveness = TYPE_EFFECTIVENESS.get(move_type, {})
        # super_effective = effectiveness.get("super_effective", [])
        # not_effective = effectiveness.get("not_effective", [])

        # Determine base damage based on move category
        if move_category == "physical":
            base_damage = move_power + self.atk - other.def_
        elif move_category == "special":
            base_damage = move_power + self.sp_atk - other.sp_def
        else:
            base_damage = move_power  # Default, in case of a non-standard category

        # Modify damage based on type effectiveness
        # if other.type in super_effective:
        #     damage_taken = base_damage * 2  # or some other multiplier
        # elif other.type in not_effective:
        #     damage_taken = base_damage * 0.5  # or some other multiplier
        # else:
        #     damage_taken = base_damage

        # Ensure damage_taken is non-negative
        # damage_taken = max(damage_taken, 0)

        # other.take_damage(damage_taken)
        # logs.log_battle(f"{self.name} attacks {other.name} for {damage_taken} damage")

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
