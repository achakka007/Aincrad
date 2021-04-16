from Armor import Armor

class RightGauntlet(Armor):
    def __init__(self):
        super().__init__()
        self.placement = "Right Hand"

class HideRightGauntlet(RightGauntlet):
    def __init__(self):
        super().__init__()
        self.name = "Hide Right Gauntlet"
        self.grade = "Common"
        self.defense = 15