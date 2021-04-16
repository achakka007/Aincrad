from Mage import ElementalMage

# LVL 50
class GrandMage(ElementalMage):
    def __init__(self):
        super().__init__()
        self.jobName = "Grand Mage"
        self.description = ""
        self.nextJobs = ["Arch Mage"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class RitualMage(ElementalMage):
    def __init__(self):
        super().__init__()
        self.jobName = "Ritual Mage"
        self.description = ""
        self.nextJobs = ["Black Magician", "Blood Magician"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class MasterOfOneXMage(ElementalMage):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Of One X Mage"
        self.description = ""
        self.nextJobs = ["Master Of Two X Mage", "Beyonder"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])

# LVL 100
class BlackMagician(RitualMage):
    def __init__(self):
        super().__init__()
        self.jobName = "Black Magician"
        self.description = ""
        self.nextJobs = ["Witch", "Vampire"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class BloodMagician(RitualMage):
    def __init__(self):
        super().__init__()
        self.jobName = "Blood Magician"
        self.description = ""
        self.nextJobs = ["Clone Creator"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])

class ArchMage(GrandMage):
    def __init__(self):
        super().__init__()
        self.jobName = "Arch Mage"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class Witch(BlackMagician):
    def __init__(self):
        super().__init__()
        self.jobName = "Witch"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class Vampire(BlackMagician):
    def __init__(self):
        super().__init__()
        self.jobName = "Vampire"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class CloneCreator(BloodMagician):
    def __init__(self):
        super().__init__()
        self.jobName = "Clone Creator"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])