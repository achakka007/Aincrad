from Job import Job

# LVL 1
class Fighter(Job):
    def __init__(self):
        super().__init__()
        self.jobName = "Fighter"
        self.description = ""
        self.nextJobs = ["Knight", "Martial Artist", "Assassin"]
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("HP", 0.5)
        ])

        def charge(self):
            return {'atkmod': 4, 'target': "Body", 'accuracy': 80, 'cost': 400, 'cooldown': 3, 'rounds passed': 0, 'debuff name': "None", 'debuff effect': "None"}

        self.attacks['charge'] = charge
        self.attackCooldowns['charge'] = 3

    

# LVL 10
class Knight(Fighter):
    def __init__(self):
        super().__init__()
        self.jobName = "Knight"
        self.description = ""
        self.nextJobs = ["Magic Swordsman", "Swordsmaster", "Dual Swordsman"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.1),
        ("Accuracy", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class MartialArtist(Fighter):
    def __init__(self):
        super().__init__()
        self.jobName = "Martial Artist"
        self.description = ""
        self.nextJobs = ["Boxer", "Kungfu", "Beserker"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.1),
        ("Defense", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Assassin(Fighter):
    def __init__(self):
        super().__init__()
        self.jobName = "Assassin"
        self.description = ""
        self.nextJobs = ["Poison User", "Ninja", "Dual Wielder"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.1),
        ("Awareness", 0.2),
        ("Stealth", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
