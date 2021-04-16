from Tank import ShieldUser

# LVL 50


class ElementalGuardian(ShieldUser):
    def __init__(self):
        super().__init__()
        self.jobName = "Elemental Guardian"
        self.description = ""
        self.nextJobs = ['Master Of One X Elemental Guardian',
                         'Grand Elemental Guardian']
        self.changeCStatBoosts([
            ("Strength", 0.3),
            ("Speed", 0.1),
            ("Stamina", 0.5),
            ("HP", 0.5),
            ("MP", 0.2),
            ("Intelligence", 0.5),
            ("Defense", 0.2)
        ])


class GreatShieldUser(ShieldUser):
    def __init__(self):
        super().__init__()
        self.jobName = "Great Shield User"
        self.description = ""
        self.nextJobs = ['Shield Hero', 'Shield Mage']
        self.changeCStatBoosts([
            ("Strength", 0.3),
            ("Speed", 0.1),
            ("Stamina", 0.5),
            ("HP", 0.5),
            ("Defense", 0.4)
        ])


class ShieldSpecialist(ShieldUser):
    def __init__(self):
        super().__init__()
        self.jobName = "Shield Specialist"
        self.description = ""
        self.nextJobs = ['Machine Shielder',
                         'Necromantic Shielder', 'Plant Shielder']
        self.changeCStatBoosts([
            ("Strength", 0.3),
            ("Speed", 0.1),
            ("Stamina", 0.5),
            ("HP", 0.5),
            ("Defense", 0.4)
        ])

# LVL 100


class MasterOfOneXElementalGuardian(ElementalGuardian):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Of One X Elemental Guardian"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
            ("Strength", 0.3),
            ("Speed", 0.1),
            ("Stamina", 0.5),
            ("HP", 0.5),
            ("MP", 0.4),
            ("Intelligence", 0.4),
            ("Defense", 0.2)
        ])


class GrandElementalGuardian(ElementalGuardian):
    def __init__(self):
        super().__init__()
        self.jobName = "Grand Elemental Guardian"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
            ("Strength", 0.3),
            ("Speed", 0.1),
            ("Stamina", 0.5),
            ("HP", 0.5),
            ("MP", 0.4),
            ("Intelligence", 0.4),
            ("Defense", 0.2)
        ])


class ShieldHero(GreatShieldUser):
    def __init__(self):
        super().__init__()
        self.jobName = "Shield Hero"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
            ("Strength", 0.3),
            ("Speed", 0.1),
            ("Stamina", 0.5),
            ("HP", 0.5),
            ("Defense", 0.4)
        ])


class ShieldMage(GreatShieldUser):
    def __init__(self):
        super().__init__()
        self.jobName = "Shield Mage"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
            ("Strength", 0.3),
            ("Speed", 0.1),
            ("Stamina", 0.5),
            ("HP", 0.5),
            ("MP", 0.4),
            ("Intelligence", 0.4),
            ("Defense", 0.2)
        ])


class MachineShielder(ShieldSpecialist):
    def __init__(self):
        super().__init__()
        self.jobName = "Machine Shielder"
        self.description = ""
        self.nextJobs = ["Walking Fortress"]
        self.changeCStatBoosts([
            ("Strength", 0.3),
            ("Speed", 0.1),
            ("Stamina", 0.5),
            ("HP", 0.5),
            ("Defense", 0.4)
        ])


class NecromanticShielder(ShieldSpecialist):
    def __init__(self):
        super().__init__()
        self.jobName = "Necromantic Shielder"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
            ("Strength", 0.3),
            ("Speed", 0.1),
            ("Stamina", 0.5),
            ("HP", 0.5),
            ("MP", 0.4),
            ("Intelligence", 0.4),
            ("Defense", 0.2)
        ])


class PlantShielder(ShieldSpecialist):
    def __init__(self):
        super().__init__()
        self.jobName = "Plant Shielder"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
            ("Strength", 0.3),
            ("Speed", 0.1),
            ("Stamina", 0.5),
            ("HP", 0.5),
            ("MP", 0.3),
            ("Intelligence", 0.3),
            ("Defense", 0.3)
        ])

# LVL 200


class WalkingFortress(MachineShielder):
    def __init__(self):
        super().__init__()
        self.jobName = "Walking Fortress"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
            ("Strength", 0.3),
            ("Speed", 0.1),
            ("Stamina", 0.5),
            ("HP", 0.5),
            ("Defense", 0.6)
        ])
