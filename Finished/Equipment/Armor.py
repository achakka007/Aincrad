
class Armor():
    elementLabels = ["Fire", "Water", "Wind", "Earth", "Dark", "Light"]
    cStatLabelList = ["HP", "MP", "Stamina", "Strength", "Speed", "Intelligence", "Defense", "Accuracy", "Acrobatics", "Stealth", "Recovery", "Awareness"] 
    oStatLabelList = ["Appraisal", "Medical Expertise", "Charisma", "Luck", "Craftsmanship", "Bargaining", "Stealing", "Experience Accumulation", "Music"]

    def __init__(self):
        self.name = "DNE"
        self.grade = "DNE"
        self.elements = []
        self.defense = 0
        self.placement = "DNE"
        self.numEnchants = 0
        self.maxNumEnchants = 0
        self.appraisalDifficulty = 0

        self.uniqFunctions = [] # List of unique function names

        self.cStatMods = []
        self.oStatMods = []

        for _cStat in self.cStatLabelList:
            self.cStatMods.append(0)
        for _oStat in self.oStatLabelList:
            self.oStatMods.append(0)

    def showDetails(self):
        print("Name:          ", self.name)
        print("Grade:         ", self.grade)
        print("Defense:       ", self.defense)
        print("Elements:      ", self.elements)
        print("Placement:     ", self.placement)
        print("Abilities:     ", self.uniqFunctions)
        print("Enchants:       {}/{}".format(self.numEnchants,self.maxNumEnchants))
        print("Appraisal Difficulty: ", self.appraisalDifficulty)
        print()


# a = Armor()
# a.showDetails()