from Fighter import Assassin

# Branch 3
# LVL 50
class PoisonUser(Assassin):
    def __init__(self):
        super().__init__()
        self.jobName = "Poison User"
        self.description = ""
        self.nextJobs = ["Elemental Assassin", "Corroder", "Shadow"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.4),
        ("Accuracy", 0.2),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Ninja(Assassin):
    def __init__(self):
        super().__init__()
        self.jobName = "Ninja"
        self.description = ""
        self.nextJobs = ["Elemental Ninja", "Ninjutsu Master", "Yin Yang User"]
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.3),
        ("Accuracy", 0.2),
        ("Acrobatics", 0.2),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class DualWielder(Assassin):
    def __init__(self):
        super().__init__()
        self.jobName = "Dual Wielder"
        self.description = ""
        self.nextJobs = ["Stone Guardian", "Weapons Master", "Time Manipulator"]
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.3),
        ("Accuracy", 0.2),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])

# LVL 100
class ElementalAssassin(PoisonUser):
    def __init__(self):
        super().__init__()
        self.jobName = "Elemental Assassin"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("MP", 0.4),
        ("Intelligence", 0.5),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Corroder(PoisonUser):
    def __init__(self):
        super().__init__()
        self.jobName = "Corroder"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.4),
        ("Accuracy", 0.2),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Shadow(PoisonUser):
    def __init__(self):
        super().__init__()
        self.jobName = "Shadow"
        self.description = ""
        self.nextJobs = ["Trickster"]
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.4),
        ("Accuracy", 0.2),
        ("Stealth", 0.4),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class ElementalNinja(Ninja):
    def __init__(self):
        super().__init__()
        self.jobName = "Elemental Ninja"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("MP", 0.4),
        ("Intelligence", 0.5),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class NinjutsuUser(Ninja):
    def __init__(self):
        super().__init__()
        self.jobName = "Ninjutsu User"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("MP", 0.2),
        ("Intelligence", 0.5),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class YinYangUser(Ninja):
    def __init__(self):
        super().__init__()
        self.jobName = "Yin Yang User"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("MP", 0.2),
        ("Intelligence", 0.5),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class StoneGuardian(DualWielder):
    def __init__(self):
        super().__init__()
        self.jobName = "Stone Guardian"
        self.description = ""
        self.nextJobs = ["GuardianDeity"]
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Defense", 0.6),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class WeaponsMaster(DualWielder):
    def __init__(self):
        super().__init__()
        self.jobName = "Weapons Master"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.3),
        ("Accuracy", 0.3),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class TimeManipulator(DualWielder):
    def __init__(self):
        super().__init__()
        self.jobName = "Time Manipulator"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("MP", 0.2),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])

# LVL 200
class Trickster(Shadow):
    def __init__(self):
        super().__init__()
        self.jobName = "Trickster"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("Intelligence", 0.5),
        ("Awareness", 0.2),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class GuardianDeity(StoneGuardian):
    def __init__(self):
        super().__init__()
        self.jobName = "Guardian Deity"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.4),
        ("Defense", 0.4),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])

