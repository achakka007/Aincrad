from Armor import Armor

class RightBoot(Armor):
    def __init__(self):
        super().__init__()
        self.placement = "Right Leg"

class HideRightBoot(RightBoot):
    def __init__(self):
        super().__init__()
        self.name = "Hide Right Boot"
        self.grade = "Common"
        self.defense = 15