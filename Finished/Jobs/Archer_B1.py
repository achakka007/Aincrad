from Archer import MasterArcher

# LVL 50
class ElementalArcher(MasterArcher):
    def __init__(self):
        super().__init__()
        self.jobName = "Elemental Archer"
        self.description = ""
        self.nextJobs = ['Master Of One X Elemental Archer', 'Spatial Manipulator']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.5),
        ("Accuracy", 0.2)
        ])
class SpecializedArcher(MasterArcher):
    def __init__(self):
        super().__init__()
        self.jobName = "Specialized Archer"
        self.description = ""
        self.nextJobs = ['Scout', 'Dealer']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.4)
        ])
class GrandArcher(MasterArcher):
    def __init__(self):
        super().__init__()
        self.jobName = "Grand Archer"
        self.description = ""
        self.nextJobs = ['Bow Master', 'Quadlauncher']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Accuracy", 0.2)
        ])

#LVL 100
class MasterOfOneXElementalArcher(ElementalArcher):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Of One X Elemental Archer"
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
class SpatialManipulator(ElementalArcher):
    def __init__(self):
        super().__init__()
        self.jobName = "Spatial Manipulator"
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
class Scout(SpecializedArcher):
    def __init__(self):
        super().__init__()
        self.jobName = "Scout"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.4),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.2)
        ])
class Dealer(SpecializedArcher):
    def __init__(self):
        super().__init__()
        self.jobName = "Dealer"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.2)
        ])
class BowMaster(GrandArcher):
    def __init__(self):
        super().__init__()
        self.jobName = "Bow Master"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.3)
        ])
class Quadlauncher(GrandArcher):
    def __init__(self):
        super().__init__()
        self.jobName = "Quadlauncher"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.2)
        ])

# LVL 200