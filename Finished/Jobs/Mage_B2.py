from Mage import SupportMage

class Healer(SupportMage): 
    def __init__(self):
        super().__init__()
        self.jobName = "Healer"
        self.description = ""
        self.nextJobs = ["Great Healer", "Master Healer", "Physician"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class GuardianMage(SupportMage):
    def __init__(self):
        super().__init__()
        self.jobName = "Guardian Mage"
        self.description = ""
        self.nextJobs = ["Tribal Guardian", "Spirit Guardian"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class Manipulator(SupportMage):
    def __init__(self):
        super().__init__()
        self.jobName = "Manipulator"
        self.description = ""
        self.nextJobs = ["Master Manipulator", "Time God"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])

class GreatHealer(Healer):
    def __init__(self):
        super().__init__()
        self.jobName = "Great Healer"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class MasterHealer(Healer):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Healer"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class Physician(Healer):
    def __init__(self):
        super().__init__()
        self.jobName = "Physician"
        self.description = ""
        self.nextJobs = ["Master Physician"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class TribalGuardian(GuardianMage):
    def __init__(self):
        super().__init__()
        self.jobName = "Tribal Guardian"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class SpiritGuardian(GuardianMage):
    def __init__(self):
        super().__init__()
        self.jobName = "Spirit Guardian"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class MasterManipulator(Manipulator):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Manipulator"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class TimeGod(Manipulator):
    def __init__(self):
        super().__init__()
        self.jobName = "Time God"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])

class MasterPhysician(Physician):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Physician"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])