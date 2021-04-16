from Armor import Armor

class Helmet(Armor):
    def __init__(self):
        super().__init__()
        self.placement = "Head"

class HideHelmet(Helmet):
    def __init__(self):
        super().__init__()
        self.name = "Hide Helmet"
        self.grade = "Common"
        self.defense = 15