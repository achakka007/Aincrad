from Job import Job

class Medic(Job):
    def __init__(self):
        super().__init__()
        self.jobName = "Medic"
        self.description = ""
        self.nextJobs = ['Healer', 'Doctor']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.2)
        ])
class Healer(Medic):
    def __init__(self):
        super().__init__()
        self.jobName = "Healer"
        self.description = ""
        self.nextJobs = ['Grand Healer', 'Elemental Healer', 'Black Healer']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.2),
        ("Medical Expertise", 0.2)
        ])
class Doctor(Medic):
    def __init__(self):
        super().__init__()
        self.jobName = "Doctor"
        self.description = ""
        self.nextJobs = ['Surgeon', 'Psychologist', 'Master Doctor']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.1),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.4)
        ])