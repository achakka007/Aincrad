from Armor import Armor

class Chestplate(Armor):
    def __init__(self):
        super().__init__()
        self.placement = "Body"

class HideChestplate(Chestplate):
    def __init__(self):
        super().__init__()
        self.name = "Hide Chestplate"
        self.grade = "Common"
        self.defense = 45 # [3 times Other Pieces]