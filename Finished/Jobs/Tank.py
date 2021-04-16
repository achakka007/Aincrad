from Job import Job

# LVL 1
class Tank(Job):
    def __init__(self):
        super().__init__()
        self.jobName = "Tank"
        self.description = ""
        self.nextJobs = ["Shield User", "Aura Practioner",]
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("HP", 0.6),
        ("Defense", 0.2)
        ])

# LVL 10
class ShieldUser(Tank):
    def __init__(self):
        super().__init__()
        self.jobName = "Shield User"
        self.description = ""
        self.nextJobs = ['Elemental Guardian', 'Great Shield User', 'Shield Specialist']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Defense", 0.4)
        ])
class AuraPractioner(Tank):
    def __init__(self):
        super().__init__()
        self.jobName = "Aura Practioner"
        self.description = ""
        self.nextJobs = ['Elemental Aura Practioner', 'Vampire Aura Practioner', 'Aura Diety']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.2),
        ("Intelligence", 0.5),
        ("Defense", 0.2)
        ])