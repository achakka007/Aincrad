from Armor import Armor

class LeftBoot(Armor):
    def __init__(self):
        super().__init__()
        self.placement = "Left Leg"

class HideLeftBoot(LeftBoot):
    def __init__(self):
        super().__init__()
        self.name = "Hide Left Boot"
        self.grade = "Common"
        self.defense = 15