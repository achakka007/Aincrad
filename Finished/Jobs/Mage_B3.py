from Mage import Summoner
# LVL 50
class SpiritBeastSummoner(Summoner):
    def __init__(self):
        super().__init__()
        self.jobName = "Spirit Beast Summoner"
        self.description = ""
        self.nextJobs = ["Spirit Beast Tamer", "Spirit Beast Slaver"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class MachineGod(Summoner):
    def __init__(self):
        super().__init__()
        self.jobName = "Machine God"
        self.description = ""
        self.nextJobs = ["Fortress King", "Swarm Queen"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class UndeadSummoner(Summoner):
    def __init__(self):
        super().__init__()
        self.jobName = "Undead Summoner"
        self.description = ""
        self.nextJobs = ["Zombie Hoarder", "Reviver"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])

# LVL 100
class SpiritBeastTamer(SpiritBeastSummoner):
    def __init__(self):
        super().__init__()
        self.jobName = "Spirit Beast Tamer"
        self.description = ""
        self.nextJobs = ["Spirit Rider"]
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class SpiritBeastSlaver(SpiritBeastSummoner):
    def __init__(self):
        super().__init__()
        self.jobName = "Spirit Beast Slaver"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class FortressKing(MachineGod):
    def __init__(self):
        super().__init__()
        self.jobName = "Fortress King"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class SwarmQueen(MachineGod):
    def __init__(self):
        super().__init__()
        self.jobName = "Swarm Queen"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class ZombieHoarder(UndeadSummoner):
    def __init__(self):
        super().__init__()
        self.jobName = "Zombie Hoarder"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])
class Reviver(UndeadSummoner):
    def __init__(self):
        super().__init__()
        self.jobName = "Reviver"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])

class SpiritRider(SpiritBeastTamer):
    def __init__(self):
        super().__init__()
        self.jobName = "Spirit Rider"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Accuracy", 0.2),
        ("Intelligence", 0.5),
        ("HP", 0.5),
        ("Stamina", 0.2),
        ("MP", 0.2)
        ])