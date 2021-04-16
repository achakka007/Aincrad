from Job import Job
# LVL 1
class Mage(Job):
    def __init__(self):
        super().__init__()
        self.jobName = "Mage"
        self.description = ""
        self.nextJobs = ["Elemental Mage", "Support Mage", "Summoner"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("MP", 0.2)
        ])

# LVL 10
class ElementalMage(Mage):
    def __init__(self):
        super().__init__()
        self.jobName = "Elemental Mage"
        self.description = ""
        self.nextJobs = ["Grand Mage", "Ritual Mage", "Master Of One X Mage"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class SupportMage(Mage):
    def __init__(self):
        super().__init__()
        self.jobName = "Support Mage"
        self.description = ""
        self.nextJobs = ["Healer", "Guardian", "Manipulator"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class Summoner(Mage):
    def __init__(self):
        super().__init__()
        self.jobName = "Summoner"
        self.description = ""
        self.nextJobs = ["Spirit Beast Summoner", "Machine God", "Undead Summoner"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])