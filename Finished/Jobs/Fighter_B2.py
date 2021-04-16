from Fighter import MartialArtist

# Branch 2
# LVL 50
class Boxer(MartialArtist):
    def __init__(self):
        super().__init__()
        self.jobName = "Boxer"
        self.description = ""
        self.nextJobs = ["Kickboxer", "Elemental Boxer", "Master Boxer"]
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("Accuracy", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Kungfu(MartialArtist):
    def __init__(self):
        super().__init__()
        self.jobName = "Kungfu"
        self.description = ""
        self.nextJobs = ["Karate", "Elemental Kungfu", "Combo Seeker"]
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("Accuracy", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Beserker(MartialArtist):
    def __init__(self):
        super().__init__()
        self.jobName = "Beserker"
        self.description = ""
        self.nextJobs = ["Pirate", "Hulk", "Axeman"]
        self.changeCStatBoosts([
        ("Strength", 0.6),
        ("Speed", 0.2),
        ("Accuracy", -0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])

# LVL 100
class Kickboxer(Boxer):
    def __init__(self):
        super().__init__()
        self.jobName = "Kickboxer"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.4),
        ("Speed", 0.2),
        ("Accuracy", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class ElementalBoxer(Boxer):
    def __init__(self):
        super().__init__()
        self.jobName = "Elemental Boxer"
        self.description = ""
        self.nextJobs = ["Spatial Guardian"]
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("MP", 0.4),
        ("Intelligence", 0.5),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class MasterBoxer(Boxer):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Boxer"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.3),
        ("Accuracy", 0.3),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Karate(Kungfu):
    def __init__(self):
        super().__init__()
        self.jobName = "Karate"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.4),
        ("Accuracy", 0.4),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class ElementalKungfu(Kungfu):
    def __init__(self):
        super().__init__()
        self.jobName = "Elemental Kungfu"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("MP", 0.4),
        ("Intelligence", 0.5),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class ComboSeeker(Kungfu):
    def __init__(self):
        super().__init__()
        self.jobName = "Combo Seeker"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Speed", 0.5),
        ("Accuracy", 0.3),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Pirate(Beserker):
    def __init__(self):
        super().__init__()
        self.jobName = "Pirate"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.3),
        ("Accuracy", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
        self.changeOStatBoost("Stealing", 0.2)
class Hulk(Beserker):
    def __init__(self):
        super().__init__()
        self.jobName = "Hulk"
        self.description = ""
        self.nextJobs = ["Frankenstein"]
        self.changeCStatBoosts([
        ("Strength", 0.4),
        ("Speed", 0.2),
        ("Defense", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Axeman(Beserker):
    def __init__(self):
        super().__init__()
        self.jobName = "Axeman"
        self.description = ""
        self.nextJobs = ["Valkyrie"]
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.2),
        ("Accuracy", 0.3),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])

# LVL 200
class SpatialGuardian(ElementalBoxer):
    def __init__(self):
        super().__init__()
        self.jobName = "Spatial Guardian"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.2),
        ("MP", 0.4),
        ("Intelligence", 0.4),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Frankenstein(Hulk):
    def __init__(self):
        super().__init__()
        self.jobName = "Frankenstein"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.4),
        ("Speed", 0.2),
        ("Accuracy", 0.1),
        ("Defense", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])
class Valkyrie(Axeman):
    def __init__(self):
        super().__init__()
        self.jobName = "Valkyrie"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.2),
        ("Speed", 0.3),
        ("Accuracy", 0.3),
        ("MP", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5)
        ])