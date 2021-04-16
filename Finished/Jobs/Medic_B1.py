from Medic import Healer

# LVL 50
class GrandHealer(Healer):
    def __init__(self):
        super().__init__()
        self.jobName = "Grand Healer"
        self.description = ""
        self.nextJobs = ['Holy Priest', 'Dragon Healer']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.7),
        ("Intelligence", 0.1),
        ("Medical Expertise", 0.1)
        ])
class ElementalHealer(Healer):
    def __init__(self):
        super().__init__()
        self.jobName = "Elemental Healer"
        self.description = ""
        self.nextJobs = ['Garnd Elemental Healer', 'Master Of One X Healer']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.2),
        ("Medical Expertise", 0.2)
        ])
class BlackHealer(Healer):
    def __init__(self):
        super().__init__()
        self.jobName = "Black Healer"
        self.description = ""
        self.nextJobs = ['Resurrectionist', 'Blood Healer']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.3),
        ("Intelligence", 0.3),
        ("Medical Expertise", 0.3)
        ])

# LVL 100
class HolyPriest(GrandHealer):
    def __init__(self):
        super().__init__()
        self.jobName = "Holy Priest"
        self.description = ""
        self.nextJobs = ["Archbishop"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.2),
        ("Medical Expertise", 0.2)
        ])
class DragonHealer(GrandHealer):
    def __init__(self):
        super().__init__()
        self.jobName = "Dragon Healer"
        self.description = ""
        self.nextJobs = ["Dragonborn"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.2),
        ("Medical Expertise", 0.2)
        ])
class GrandElementalHealer(ElementalHealer):
    def __init__(self):
        super().__init__()
        self.jobName = "Grand Elemental Healer"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.6),
        ("Intelligence", 0.2),
        ("Medical Expertise", 0.1)
        ])
class MasterOfOneXHealer(ElementalHealer):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Of One X Healer"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.4),
        ("Intelligence", 0.3),
        ("Medical Expertise", 0.2)
        ])
class Resurrectionist(BlackHealer):
    def __init__(self):
        super().__init__()
        self.jobName = "Resurrectionist"
        self.description = ""
        self.nextJobs = ["Mass Resurrectionist"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.3),
        ("Intelligence", 0.4),
        ("Medical Expertise", 0.2)
        ])
class BloodHealer(BlackHealer):
    def __init__(self):
        super().__init__()
        self.jobName = "Blood Healer"
        self.description = ""
        self.nextJobs = ["Vampire Priest"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.3),
        ("Intelligence", 0.3),
        ("Medical Expertise", 0.3)
        ])

# LVL 200
class Archbishop(HolyPriest):
    def __init__(self):
        super().__init__()
        self.jobName = "Archbishop"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.4),
        ("Medical Expertise", 0.2)
        ])
class Dragonborn(DragonHealer):
    def __init__(self):
        super().__init__()
        self.jobName = "Dragonborn"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.7),
        ("Intelligence", 0.2),
        ("Medical Expertise", 0.2)
        ])
class MassRessurectionist(Resurrectionist):
    def __init__(self):
        super().__init__()
        self.jobName = "Mass Ressurectionist"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.4),
        ("Medical Expertise", 0.2)
        ])
class VampirePriest(BloodHealer):
    def __init__(self):
        super().__init__()
        self.jobName = "Vampire Priest"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.4),
        ("Medical Expertise", 0.2)
        ])