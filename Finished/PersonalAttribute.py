from Labels import Labels
class PersonalAttribute:

    cStatLabels = Labels.cStatLabelList
    oStatLabels =  Labels.oStatLabelList

    def __init__(self, name = "DNE", description = "DNE"):
        self.name = name
        self.description = description

        self.cStatPMods = [] # Array of Doubles
        self.oStatPMods = [] # Array of Doubles
        self.cStatAMods = [] # Array of Doubles
        self.oStatAMods = [] # Array of Doubles

        # print("-------- {}".format(len(self.cStatLabels)))
        for _i in range(0,len(PersonalAttribute.cStatLabels) + 0):
            self.cStatPMods.append(1)
        for _i in range(0,len(PersonalAttribute.oStatLabels) + 0):
            self.oStatPMods.append(1)
        
        for _i in range(0,len(PersonalAttribute.cStatLabels) + 0):
            self.cStatAMods.append(1)
        for _i in range(0,len(PersonalAttribute.oStatLabels) + 0):
            self.oStatAMods.append(1)

        # print(self.cStatPMods)

    def showDescription(self):
        print("Description: {}".format(self.description))

    def showName(self):
        print("Name: {}".format(self.name))

    def showStatMods(self):
        print("Combat Stat Mods(Passive):")
        for i in range (0,len(self.cStatLabels)):
            print("{} = {}".format(self.cStatLabels[i], self.cStatPMods[i]))
        print("\nOther Stats:")
        for i in range (0,len(self.oStatLabels)):
            print("{} = {}".format(self.oStatLabels[i], self.oStatPMods[i]))

        print("Combat Stat Mods(Active):")
        for i in range (0,len(self.cStatLabels)):
            print("{} = {}".format(self.cStatLabels[i], self.cStatAMods[i]))
        print("\nOther Stats:")
        for i in range (0,len(self.oStatLabels)):
            print("{} = {}".format(self.oStatLabels[i], self.oStatAMods[i]))

    def changeCStatPMod(self, statName, num):
        self.cStatPMods[self.cStatLabels.index(statName)] += num

    def changeOStatPMod(self, statName, num):
        #import pdb
        #pdb.set_trace()
        self.oStatPMods[self.oStatLabels.index(statName)] += num

    def changeCStatAMod(self, statName, num):
        self.cStatAMods[self.cStatLabels.index(statName)] += num

    def changeOStatAMod(self, statName, num):
        self.oStatAMods[self.oStatLabels.index(statName)] += num

    def changeCStatPMods(self, lis):
        for pair in lis:
            self.changeCStatPMod(pair[0], pair[1])

    def changeOStatPMods(self, lis):
        for pair in lis:
            self.changeOStatPMod(pair[0], pair[1])

    def changeCStatAMods(self, lis):
        for pair in lis:
            self.changeCStatAMod(pair[0], pair[1])

    def changeOStatAMods(self, lis):
        for pair in lis:
            self.changeOStatAMod(pair[0], pair[1])

    def isActive(self, OrigUser = None, CurrUser = None, **kwargs):
        return False

    def isDeActive(self, OrigUser = None, CurrUser = None, **kwargs):
        return False
