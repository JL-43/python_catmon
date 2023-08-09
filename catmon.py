from typing import Dict, List

from config import TYPE_EFFECTIVENESS
from logs import Logs
from move import Move

logs = Logs()


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
        if selected_move.category == "heal":  # heal move
            heal_amount: int = selected_move.power
            self.heal(heal_amount)
        else:  # attack (physical or special) move
            self.attack(
                other,
                selected_move.name,
                selected_move.power,
                selected_move.category,
                selected_move.move_type,
            )

    def attack(
        self,
        other: "Catmon",
        move_name: str,
        move_power: float,
        move_category: str,
        move_type: str,
    ):
        effectiveness: dict = TYPE_EFFECTIVENESS.get(move_type, {})  # type: ignore

        super_effective: list = effectiveness.get("super_effective", [])
        not_effective: list = effectiveness.get("not_effective", [])

        log_string_1: str = f"{self.name} attacks {other.name} with {move_name} for"

        logs.log_battle(str(effectiveness))
        logs.log_battle(f"Super effective against: {super_effective}")
        logs.log_battle(f"Not very effective against: {not_effective}")

        # Determine base damage based on move category
        base_damage: float = 0
        if move_category == "physical":
            base_damage = move_power + self.atk - other.def_
        elif move_category == "special":
            base_damage = move_power + self.sp_atk - other.sp_def
        else:
            base_damage = move_power  # Default, in case of a non-standard category

        # Modify damage based on type effectiveness
        log_string_3: str = ""
        damage_taken: int = 0
        if other.type in super_effective:
            damage_taken = int(base_damage * 2)  # or some other multiplier
            log_string_3 = ". It's super effective!"
        elif other.type in not_effective:
            damage_taken = int(base_damage * 0.5)  # or some other multiplier
            log_string_3 = ". It's not very effective."
        else:
            damage_taken = int(base_damage)

        # Ensure damage_taken is non-negative
        damage_taken = max(damage_taken, 0)
        log_string_2: str = f" {damage_taken} damage"

        log_string: str = f"{log_string_1}{log_string_2}{log_string_3}"

        # other.take_damage(damage_taken)
        logs.log_battle(log_string)

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
