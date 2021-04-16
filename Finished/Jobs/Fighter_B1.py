from Fighter import Knight

# Branch 1
# LVL 50
class MagicSwordsman(Knight):
    def __init__(self):
        super().__init__()
        self.jobName = "Magic Swordsman"
        self.description = ""
        self.nextJobs = ["Elemental Swordsman", "Illusionary Swordsman", "Enhancer Swordsman"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.1),
        ("MP", 0.5),
        ("Intelligence", 0.5),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Swordsmaster(Knight):
    def __init__(self):
        super().__init__()
        self.jobName = "Swordsmaster"
        self.description = ""
        self.nextJobs = ["Sword Grandmaster", "Swordartist", "Breaker"]
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("Accuracy", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class DualSwordsman(Knight):
    def __init__(self):
        super().__init__()
        self.jobName = "Dual Swordsman"
        self.description = ""
        self.nextJobs = ["Magic Dual Swordsman", "Tri Swordsman", "Blade Dancer"]
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("Acrobatics", 0.5),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])

# LVL 100
class ElementalSwordsman(MagicSwordsman):
    def __init__(self):
        super().__init__()
        self.jobName = "Elemental Swordsman"
        self.description = ""
        self.nextJobs = ["Spirit Champion"]
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("MP", 0.2),
        ("Intelligence", 0.5),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class IllusionarySwordsman(MagicSwordsman):
    def __init__(self):
        super().__init__()
        self.jobName = "Illusionary Swordsman"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("MP", 0.2),
        ("Intelligence", 0.5),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class EnhancerSwordsman(MagicSwordsman): 
    def __init__(self):
        super().__init__()
        self.jobName = "Enhancer Swordsman"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("MP", 0.4),
        ("Intelligence", 0.4),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class SwordGrandmaster(Swordsmaster):
    def __init__(self):
        super().__init__()
        self.jobName = "Sword Grandmaster"
        self.description = ""
        self.nextJobs = ["Rider", "Sword King"]
        self.changeCStatBoosts([
        ("Strength", 0.4),
        ("Speed", 0.4),
        ("Accuracy", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class SwordArtist(Swordsmaster):
    def __init__(self):
        super().__init__()
        self.jobName = "Sword Artist"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.4),
        ("Accuracy", 0.4),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Breaker(Swordsmaster):
    def __init__(self):
        super().__init__()
        self.jobName = "Breaker"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.4),
        ("Speed", 0.4),
        ("Accuracy", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class MagicDualSwordsman(DualSwordsman):
    def __init__(self):
        super().__init__()
        self.jobName = "Magic Dual Swordsman"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("MP", 0.4),
        ("Intelligence", 0.5),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class TriSwordsman(DualSwordsman):
    def __init__(self):
        super().__init__()
        self.jobName = "Tri Swordsman"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.4),
        ("Speed", 0.2),
        ("Accuracy", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class BladeDancer(DualSwordsman):
    def __init__(self):
        super().__init__()
        self.jobName = "Blade Dancer"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.4),
        ("Acrobatics", 0.4),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])

# LVL 200
class SpiritChampion(ElementalSwordsman):
    def __init__(self):
        super().__init__()
        self.jobName = "Spirit Champion"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("MP", 0.2),
        ("Intelligence", 0.5),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Rider(SwordGrandmaster):
    def __init__(self):
        super().__init__()
        self.jobName = "Rider"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.4),
        ("Speed", 0.2),
        ("Accuracy", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class SwordKing(SwordGrandmaster):
    def __init__(self):
        super().__init__()
        self.jobName = "Sword King"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.4),
        ("Accuracy", 0.4),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])