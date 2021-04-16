from Armor import Armor

class LeftGauntlet(Armor):
    def __init__(self):
        super().__init__()
        self.placement = "Left Hand"

class HideLeftGauntlet(LeftGauntlet):
    def __init__(self):
        super().__init__()
        self.name = "Hide Left Gauntlet"
        self.grade = "Common"
        self.defense = 15