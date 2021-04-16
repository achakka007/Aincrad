from Archer import SlingshotUser

# LVL 50
class ExplosiveExpert(SlingshotUser):
    def __init__(self):
        super().__init__()
        self.jobName = "Explosive Expert"
        self.description = ""
        self.nextJobs = ['Destroyer']
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.2)
        ])
class PlantExpert(SlingshotUser):
    def __init__(self):
        super().__init__()
        self.jobName = "Plant Expert"
        self.description = ""
        self.nextJobs = ['One With Nature', 'Magic Plant Expert']
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.3),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.2)
        ])
class MagicExpert(SlingshotUser):
    def __init__(self):
        super().__init__()
        self.jobName = "Magic Expert"
        self.description = ""
        self.nextJobs = ['Slingshot Mage', 'Slingshot Deity']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.5),
        ("Accuracy", 0.2)
        ])

# LVL 100
class Destroyer(ExplosiveExpert):
    def __init__(self):
        super().__init__()
        self.jobName = "Destroyer"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.2)
        ])
class OneWithNature(PlantExpert):
    def __init__(self):
        super().__init__()
        self.jobName = "One With Nature"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.3),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.2)
        ])
class MagicPlantExpert(PlantExpert):
    def __init__(self):
        super().__init__()
        self.jobName = "Magic Plant Expert"
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
class SlingshotMage(MagicExpert):
    def __init__(self):
        super().__init__()
        self.jobName = "Slingshot Mage"
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
class SlingshotDeity(MagicExpert):
    def __init__(self):
        super().__init__()
        self.jobName = "Slingshot Deity"
        self.description = ""
        self.nextJobs = ["Slingshot God"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.5),
        ("Accuracy", 0.2)
        ])

# LVL 200
class SlingshotGod(SlingshotDeity):
    def __init__(self):
        super().__init__()
        self.jobName = "Slingshot God"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.5),
        ("Accuracy", 0.3)
        ])