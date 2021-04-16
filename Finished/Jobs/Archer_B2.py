from Archer import GunLord

#LVL 50
class Sniper(GunLord):
    def __init__(self):
        super().__init__()
        self.jobName = "Sniper"
        self.description = ""
        self.nextJobs = ['Master Sniper', 'Magic Sniper']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.4)
        ])
class MagicPistolUser(GunLord):
    def __init__(self):
        super().__init__()
        self.jobName = "Magic Pistol User"
        self.description = ""
        self.nextJobs = ['Dual Pistols', 'Gun Mage']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.5),
        ("Accuracy", 0.2)
        ])
class Gunner(GunLord):
    def __init__(self):
        super().__init__()
        self.jobName = "Gunner"
        self.description = ""
        self.nextJobs = ['Missile Master', 'Expert Gunner']
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.2)
        ])

# LVL 100
class MasterSniper(Sniper):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Sniper"
        self.description = ""
        self.nextJobs = ["Sniper Legend"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.4)
        ])
class MagicSniper(Sniper):
    def __init__(self):
        super().__init__()
        self.jobName = "Magic Sniper"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.5),
        ("Accuracy", 0.2)
        ])
class DualPistols(MagicPistolUser):
    def __init__(self):
        super().__init__()
        self.jobName = "Dual Pistols"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Accuracy", 0.2)
        ])
class GunMage(MagicPistolUser):
    def __init__(self):
        super().__init__()
        self.jobName = "Gun Mage"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.5),
        ("Accuracy", 0.2)
        ])
class MissileMaster(Gunner):
    def __init__(self):
        super().__init__()
        self.jobName = "Missile Master"
        self.description = ""
        self.nextJobs = ["Atomic Weaponsmaster"]
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.2)
        ])
class ExpertGunner(Gunner):
    def __init__(self):
        super().__init__()
        self.jobName = "Expert Gunner"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.3)
        ])

# LVL 200
class SniperLegend(MasterSniper):
    def __init__(self):
        super().__init__()
        self.jobName = "Sniper Legend"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.6)
        ])
class AtomicWeaponsmaster(MissileMaster):
    def __init__(self):
        super().__init__()
        self.jobName = "Atomic Weaponsmaster"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.5),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.2)
        ])