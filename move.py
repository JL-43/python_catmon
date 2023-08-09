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
