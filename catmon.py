from typing import List, Tuple

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
        nickname: str,
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
    ) -> None:
        self.name = name
        self.nickname = nickname
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
    ) -> None:
        base_damage = self.calculate_base_damage(other, move_power, move_category)
        type_multiplier, type_log = self.calculate_type_effectiveness(other, move_type)
        final_damage = int(base_damage * type_multiplier)
        final_damage = max(final_damage, 0)

        log_string = f"{self.nickname} attacks {other.nickname} with {move_name} for {final_damage} damage{type_log}"
        logs.log_battle(log_string)
        other.take_damage(final_damage)

    def calculate_base_damage(
        self, other: "Catmon", move_power: float, move_category: str
    ) -> float:
        if move_category == "physical":
            return move_power + self.atk - other.def_
        elif move_category == "special":
            return move_power + self.sp_atk - other.sp_def
        else:
            return move_power

    def calculate_type_effectiveness(
        self, other: "Catmon", move_type: str
    ) -> Tuple[float, str]:
        effectiveness = TYPE_EFFECTIVENESS.get(move_type, {})
        # mypy doesnt think these have "get" methods
        super_effective = effectiveness.get("super_effective", [])  # type: ignore
        not_effective = effectiveness.get("not_effective", [])  # type: ignore
        if other.type in super_effective:
            return 2, ". It's super effective!"
        elif other.type in not_effective:
            return 0.5, ". It's not very effective."
        else:
            return 1, ""

    def calculate_damage(
        self, other: "Catmon", move_power: float, move_category: str, move_type: str
    ) -> Tuple[float, str]:
        base_damage = self.calculate_base_damage(other, move_power, move_category)
        type_multiplier, type_log = self.calculate_type_effectiveness(other, move_type)
        return base_damage * type_multiplier, type_log

    def take_damage(self, damage_taken: int) -> None:
        self.health -= damage_taken

    def heal(self, heal_amount: int) -> None:
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

    def display_stats(self) -> None:
        for attribute, value in vars(self).items():
            print(f"{attribute}: {value}")

    def display_moves(self) -> None:
        print("Moves:")
        for move in self.moves:
            print(f"  - {move}")
