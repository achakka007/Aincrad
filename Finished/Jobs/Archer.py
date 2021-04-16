from Job import Job
# LVL 1
class Archer(Job):
    def __init__(self):
        super().__init__()
        self.jobName = "Archer"
        self.description = ""
        self.nextJobs = ['Master Archer', 'Gun Lord', 'Slingshot User']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.3),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.2)
        ])

# LVL 10
class MasterArcher(Archer):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Archer"
        self.description = ""
        self.nextJobs = ['Elemental Archer', 'Specialized Archer', 'Grand Archer']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.3)
        ])
class GunLord(Archer):
    def __init__(self):
        super().__init__()
        self.jobName = "Gun Lord"
        self.description = ""
        self.nextJobs = ['Sniper', 'Magic Pistol User', 'Gunner']
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.2)
        ])
class SlingshotUser(Archer):
    def __init__(self):
        super().__init__()
        self.jobName = "Slingshot User"
        self.description = ""
        self.nextJobs = ['Explosive Expert', 'Plant Expert', 'Magic Expert']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Accuracy", 0.3)
        ])