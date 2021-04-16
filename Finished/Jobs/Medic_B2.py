from Medic import Doctor

# LVL 50
class Surgeon(Doctor):
    def __init__(self):
        super().__init__()
        self.jobName = "Surgeon"
        self.description = ""
        self.nextJobs = ['Battle Surgeon', 'Master Surgeon']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.4)
        ])
class Psychologist(Doctor):
    def __init__(self):
        super().__init__()
        self.jobName = "Psychologist"
        self.description = ""
        self.nextJobs = ['Chief Psychologist', 'Neurosurgeon']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.4)
        ])
class MasterDoctor(Doctor):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Doctor"
        self.description = ""
        self.nextJobs = ['Master Clinician', 'Cyborg Specialist']
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.4)
        ])

# LVL 100
class BattleSurgeon(Surgeon):
    def __init__(self):
        super().__init__()
        self.jobName = "Battle Surgeon"
        self.description = ""
        self.nextJobs = ["Veteran Surgeon"]
        self.changeCStatBoosts([
        ("Strength", 0.3),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.2)
        ])
class MasterSurgeon(Surgeon):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Surgeon"
        self.description = ""
        self.nextJobs = ["Doctor Of The Dead"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.4)
        ])
class ChiefPsychologist(Psychologist):
    def __init__(self):
        super().__init__()
        self.jobName = "Chief Psychologist"
        self.description = ""
        self.nextJobs = ["Master Psychologist"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.4)
        ])
class Neurosurgeon(Psychologist):
    def __init__(self):
        super().__init__()
        self.jobName = "Neurosurgeon"
        self.description = ""
        self.nextJobs = ["Mind Master"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.4)
        ])
class MasterClinician(MasterDoctor):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Clinician"
        self.description = ""
        self.nextJobs = ["Chronodoc"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.4)
        ])
class CyborgSpecialist(MasterDoctor):
    def __init__(self):
        super().__init__()
        self.jobName = "Cyborg Specialist"
        self.description = ""
        self.nextJobs = ["Nanotech Expert", "Priest General"]
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.4)
        ])

# LVL 200
class VeteranSurgeon(BattleSurgeon):
    def __init__(self):
        super().__init__()
        self.jobName = "Veteran Surgeon"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.6)
        ])
class DoctorOfTheDead(MasterSurgeon):
    def __init__(self):
        super().__init__()
        self.jobName = "Doctor Of The Dead"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.6)
        ])
class MasterPsychologist(ChiefPsychologist):
    def __init__(self):
        super().__init__()
        self.jobName = "Master Psychologist"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.6)
        ])
class MindMaster(Neurosurgeon):
    def __init__(self):
        super().__init__()
        self.jobName = "Mind Master"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.6)
        ])
class Chronodoc(MasterClinician):
    def __init__(self):
        super().__init__()
        self.jobName = "Chronodoc"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("MP", 0.5),
        ("Intelligence", 0.4),
        ("Medical Expertise", 0.2)
        ])
class NanotechExpert(CyborgSpecialist):
    def __init__(self):
        super().__init__()
        self.jobName = "Nanotech Expert"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.6)
        ])
class PriestGeneral(CyborgSpecialist):
    def __init__(self):
        super().__init__()
        self.jobName = "Priest General"
        self.description = ""
        self.nextJobs = []
        self.changeCStatBoosts([
        ("Strength", 0.1),
        ("Speed", 0.2),
        ("Stamina", 0.5),
        ("HP", 0.5),
        ("Medical Expertise", 0.6)
        ])