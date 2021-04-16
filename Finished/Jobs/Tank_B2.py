from Tank import AuraPractioner

# LVL 50
class ElementalAuraPractioner(AuraPractioner):
    def __init__(self):
        super().__init__()
        self.jobName = "Elemental Aura Practioner"
        self.description = ""
        self.nextJobs = ['Grand Aura Practioner', 'Master Of One X Aura Practioner']
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.2),
        ("Intelligence", 0.3),
        ("Defense", 0.2)
        ])
class VampireAuraPractioner(AuraPractioner):
    def __init__(self):
        super().__init__()
        self.jobName = "Vampire Aura Practioner"
        self.description = ""
        self.nextJobs = ['High Vampire Aura Practioner']
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.2),
        ("Intelligence", 0.3),
        ("Defense", 0.2)
        ])
class AuraDiety(AuraPractioner):
    def __init__(self):
        super().__init__()
        self.jobName = "Aura Diety"
        self.description = ""
        self.nextJobs = ['Aura God', 'Aura Demon']
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.3),
        ("Intelligence", 0.3),
        ("Defense", 0.1)
        ])

# LVL 100

class GrandAuraPractioner(ElementalAuraPractioner):
    def __init__(self):
        super().__init__()
        self.jobName = "Grand Aura Practioner"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.4),
        ("Intelligence", 0.5),
        ("Defense", 0.2)
        ])
class MasterOfOneXAuraPractioner(ElementalAuraPractioner):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Of One X Aura Practioner"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.4),
        ("Intelligence", 0.5),
        ("Defense", 0.2)
        ])
class HighVampireAuraPractioner(VampireAuraPractioner):
    def __init__(self):
        super().__init__()
        self.jobName = "High Vampire Aura Practioner"
        self.description = ""
        self.nextJobs = ["Vampire Aura Lord"]
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.4),
        ("Intelligence", 0.5),
        ("Defense", 0.2)
        ])
class AuraGod(AuraDiety):
    def __init__(self):
        super().__init__()
        self.jobName = "Aura God"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.4),
        ("Intelligence", 0.6),
        ("Defense", 0.1)
        ])
class AuraDemon(AuraDiety):
    def __init__(self):
        super().__init__()
        self.jobName = "Aura Demon"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Intelligence", 0.4),
        ("MP", 0.6)
        ])

# LVL 200
class VampireAuraLord(HighVampireAuraPractioner):
    def __init__(self):
        super().__init__()
        self.jobName = "Vampire Aura Lord"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.6),
        ("Intelligence", 0.5),
        ("Defense", 0.2)
        ])

# LVL 300
class VampireKing(VampireAuraLord):
    def __init__(self):
        super().__init__()
        self.jobName = "Vampire King"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.4),
        ("Intelligence", 0.5),
        ("Defense", 0.2)
        ])
