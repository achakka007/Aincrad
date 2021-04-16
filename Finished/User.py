import random
import copy
from Labels import Labels

from Job import Job
from PersonalAttribute import PersonalAttribute
from PersonalAttributes import *

# from Chestplate import *
# from Helmet import *
# from LeftBoot import *
# from RightBoot import *
# from LeftGauntlet import *
# from RightGauntlet import *

from Jobs.Fighter import Fighter
# from Fighter_B1 import *
# from Fighter_B2 import *
# from Fighter_B3 import *

from Jobs.Mage import Mage
# from Mage_B1 import *
# from Mage_B2 import *
# from Mage_B3 import *

from Jobs.Tank import Tank
# from Tank_B1 import *
# from Tank_B2 import *

from Jobs.Archer import Archer
# from Archer_B1 import *
# from Archer_B2 import *
# from Archer_B3 import *

from Jobs.Medic import Medic
# from Medic_B1 import *
# from Medic_B2 import *


class User:

    traitLabelList = Labels.traitLabelList
    elementLabelList = Labels.elementLabelList

    cStatLabelList = Labels.cStatLabelList
    oStatLabelList = Labels.oStatLabelList

    userPersonalAttributes = [TrailBlazer, AbsoluteLuck, Sage,
                              Genius, Idol, Phantom, SilverTongue, FastOnYourFeet, Clutch]
    userBodyPartLabels = Labels.userBodyPartLabels

    def __init__(self, **kwargs):
        origUser = kwargs.get('User')
        userType = kwargs.get('Type')
        name = kwargs.get('Name')
        job = kwargs.get('Job')
        self.username = ""
        self.level = 0
        self.userJob = None
        self.userTraits = []
        self.userElements = []
        self.userBaseCStats = []
        self.userBaseOStats = []
        self.userCStats = []
        self.userOStats = []
        self.hPSplit = []
        self.armor = []
        self.userPersonalAttribute = None  # = PersonalAttribute()

        if userType == "Real":
            self.setLevel(1)

            self.setName(self.inputName())
            input("Press Enter to continue")

            self.setJob(self.inputJob())
            input("Press Enter to continue")

            self.setTraits()
            self.showTraits()
            input("Press Enter to continue")

            self.setBaseStats()
            self.showBaseStats()
            input("Press Enter to continue")

            self.setPersonalAttribute()
            self.showPersonalAttribute()
            input("Press Enter to continue")

            self.setElements()
            self.showElements()

            self.setStats()
            self.setHPSplit()
            self.setArmor()

        elif userType == "NPC":
            self.setLevel(1)
            self.setName(name)
            self.setJob(job)
            self.setTraits()
            self.setBaseStats()
            self.setPersonalAttribute()
            self.setStats()
            self.setHPSplit()
            self.setArmor()
            self.setElements()

        elif userType == "Copy":
            self.level = origUser.level
            self.username = origUser.username
            self.userJob = origUser.userJob
            self.userTraits = copy.copy(origUser.userTraits)
            self.userBaseCStats = copy.copy(origUser.userBaseCStats)
            self.userBaseOStats = copy.copy(origUser.userBaseOStats)
            self.userPersonalAttribute = origUser.userPersonalAttribute
            self.userCStats = copy.copy(origUser.userCStats)
            self.userOStats = copy.copy(origUser.userOStats)
            self.hPSplit = copy.copy(origUser.hPSplit)
            self.armor = copy.copy(origUser.armor)
            self.userElements = copy.copy(origUser.userElements)

        else:
            pass

    # Build Functions
    def inputName(self):
        print("Welcome to my VR World!")
        return input("What is your name? ")

    def setName(self, name="DNE"):
        self.username = name

    def setLevel(self, lvl=0):
        self.level = lvl

    def inputJob(self):
        print("\nHello {}. Here is a list of classes for you to choose from:".format(
            self.username))
        commonClassList = ["Fighter", "Mage", "Medic", "Tank", "Archer"]
        rareClassList = ["Spearman", "Alchemist",
                         "Craftsman", "Musician", "Cook"]
        uniqueClassList = ["Gambler", "Tamer"]
        userClassRarity = random.randint(1, 100)
        allowedClasses = [] + commonClassList
        if userClassRarity > 90:
            uniqueClass = uniqueClassList[random.randint(
                0, len(uniqueClassList) - 1)]
            allowedClasses.append(uniqueClass)
            print("Unique Class => ['{}']".format(uniqueClass))
        if userClassRarity > 50:
            rareClass = rareClassList[random.randint(
                0, len(rareClassList) - 1)]
            allowedClasses.append(rareClass)
            print("Rare Class   => ['{}']".format(rareClass))
        print("Common Class =>", commonClassList)
        userJob = input("\nWhich class would you like to choose? ")
        if userJob not in allowedClasses:
            print("ERROR - Class Not Found")
            exit()  # User has chosen an invalid class
        print("You are now a {}".format(userJob))
        return userJob

    def setJob(self, job=None):
        self.userJob = eval(job)()

    def setTraits(self):

        eyeList = ["Byakugan", "Sharingan", "Demonic Eyes", "Appraisal",
                   "Time Manipulation", "Seer", "Laser", "Hypersensitivity"]
        self.userTraits.append(eyeList[random.randint(
            0, len(eyeList) - 1)] if (random.randint(1, 100) > 95) else "None")

        skinList = ["Steel Skin", "Scales", "Hardened", "Bark",
                    "Chameleon", "Mimic", "Shell", "Elementalized"]
        self.userTraits.append(skinList[random.randint(
            0, len(skinList) - 1)] if (random.randint(1, 100) > 95) else "None")

        coreList = ["Electrium", "Dragon's Heart",
                    "Demon's Heart", "Soul Manifest"]
        self.userTraits.append(coreList[random.randint(
            0, len(coreList) - 1)] if (random.randint(1, 100) > 95) else "None")

        nailList = ["Elongation", "Transmutation",
                    "Projectile", "Elementalized"]
        self.userTraits.append(nailList[random.randint(
            0, len(nailList) - 1)] if (random.randint(1, 100) > 95) else "None")

        hairList = ["Elongation", "Transmutation",
                    "Projectile", "Elementalized"]
        self.userTraits.append(hairList[random.randint(
            0, len(hairList) - 1)] if (random.randint(1, 100) > 95) else "None")

        earList = ["Hypersensitvity", "Multilingual"]
        self.userTraits.append(earList[random.randint(
            0, len(earList) - 1)] if (random.randint(1, 100) > 95) else "None")

        noseList = ["Hypersensitvity"]
        self.userTraits.append(noseList[random.randint(
            0, len(noseList) - 1)] if (random.randint(1, 100) > 95) else "None")

        mouthList = ["Fangs", "Reinforced",
                     "Gifted Singer", "Echolocation", "Shriek"]
        self.userTraits.append(mouthList[random.randint(
            0, len(mouthList) - 1)] if (random.randint(1, 100) > 95) else "None")

        otherList = ["Bone Control", "Plant Fusion",
                     "Animal Fusion", "Iron Lung", "Gills", "Wings", "Tail"]
        self.userTraits.append(otherList[random.randint(
            0, len(otherList) - 1)] if (random.randint(1, 100) > 99) else "None")

    def showTraits(self):
        i = 0
        for trait in self.userTraits:
            print("{}: {}".format(self.traitLabelList[i], trait))
            i += 1

    def setBaseStats(self):
        for _i in range(0, 3):
            self.userBaseCStats.append(random.randint(800, 1000))

        for _i in range(3, len(self.cStatLabelList)):
            self.userBaseCStats.append(random.randint(8, 10))

        for _i in range(0, len(self.oStatLabelList)):
            self.userBaseOStats.append(random.randint(1, 10))

    def showBaseStats(self):
        print("\nHere are the stats you have been bestowed upon by the system:")
        print("Combat Stats:")
        for i in range(0, len(self.cStatLabelList)):
            print("{} = {}".format(
                self.cStatLabelList[i], self.userBaseCStats[i]))
        print("\nOther Stats:")
        for i in range(0, len(self.oStatLabelList)):
            print("{} = {}".format(
                self.oStatLabelList[i], self.userBaseOStats[i]))

    def setPersonalAttribute(self):
        self.userPersonalAttribute = self.userPersonalAttributes[random.randint(
            0, len(self.userPersonalAttributes)-1)]

    def showPersonalAttribute(self):
        print(self.userPersonalAttribute.description)
        print("Your personal attribute is: {}".format(
            self.userPersonalAttribute.name))

    def setStats(self):
        for i in range(0, len(self.cStatLabelList)):
            self.userCStats.append(
                self.userBaseCStats[i] * self.userJob.cStatBoosts[i] * self.userPersonalAttribute.cStatPMods[i])
        for i in range(0, len(self.oStatLabelList)):
            self.userOStats.append(
                self.userBaseOStats[i] * self.userJob.oStatBoosts[i] * self.userPersonalAttribute.oStatPMods[i])

    def setElements(self):
        for _i in range(0, len(self.elementLabelList)):
            self.userElements.append(False)
        for _i in range(0, len(self.elementLabelList)):
            if (random.randint(1, 100) > 95):
                self.userElements[_i] = True

    def showElements(self):
        arr = []
        for i in range(0, len(self.elementLabelList)):
            if self.userElements[i]:
                arr.append(self.elementLabelList[i])
        print("User Elements: {}".format(arr))

    def setHPSplit(self):
        hP = self.getHealth()
        self.hPSplit.append(round(hP * 0.3))  # HEAD
        self.hPSplit.append(round(hP * 0.3))  # BODY
        self.hPSplit.append(round(hP * 0.1))
        self.hPSplit.append(round(hP * 0.1))
        self.hPSplit.append(round(hP * 0.1))
        self.hPSplit.append(round(hP * 0.1))

        # hP = self.getHealth() / len(self.userBodyPartLabels)
        # for _i in range(0,len(self.userBodyPartLabels)):
        #     self.hPSplit.append(hP)

    def setArmor(self):
        for _i in range(0, len(self.userBodyPartLabels)):
            self.armor.append(None)

    # Helper Functions
    def getTrait(self, traitName):
        return self.userTraits[self.traitLabelList.index(traitName)]

    def getCStat(self, statName):
        return self.userCStats[self.cStatLabelList.index(statName)]

    def getOStat(self, statName):
        return self.userOStats[self.oStatLabelList.index(statName)]

    def getHealth(self):
        return self.getCStat("HP")

    def getAttack(self):
        return (self.getCStat("Strength") * self.getCStat("Speed"))

    def getDefense(self, target):
        return self.getCStat("Defense") * 3 + self.getArmorDefense(target)

    def getArmorDefense(self, target):
        armorPiece = self.armor[self.userBodyPartLabels.index(target)]
        return 0 if armorPiece is None else armorPiece.defense

    def getBodyPartHealth(self, target):
        return self.hPSplit[self.userBodyPartLabels.index(target)]

    def getArmorList(self):
        armorList = []
        for armorPiece in self.armor:
            if armorPiece is None:
                armorList.append("None")
            else:
                armorList.append(armorPiece.name)
        return armorList

    def getStamina(self):
        return self.getCStat('Stamina')

    # ADMIN FUNCTIONS
    def showUser(self):
        print("[")
        print("Name = {}".format(self.username))
        print("Personal Attribute = {}".format(
            self.userPersonalAttribute.name))
        print("Health = {}".format(round(self.getHealth())))
        print("Attack = {}".format(self.getAttack()))
        print("Stamina = {}".format(self.getStamina()))
        # print("Defense(Head) = {}".format(self.getDefense("Head")))
        # print("Armor =  {}".format(self.getArmorList()))
        # self.showElements()
        print("]")

    def upgradeJob(self):
        if(len(self.userJob.nextJobs) > 0):
            print("Here are you next jobs: {}".format(self.userJob.nextJobs))
            self.userJob = eval(input("Choose: ").replace(" ", ""))()
        else:
            print("No further jobs available")

    def equipArmor(self, armorPiece):
        item = eval(armorPiece.replace(" ", ""))()
        self.armor[self.userBodyPartLabels.index(item.placement)] = item

    # COMBAT FUNCTIONS
    def changeHealth(self, change, target):
        bodyPart = self.userBodyPartLabels.index(target)
        self.hPSplit[bodyPart] = round(self.hPSplit[bodyPart] + change)
        if self.hPSplit[bodyPart] < 0:
            self.hPSplit[bodyPart] = 0
            self.updateTotalHP()
            return True  # If body part is disabled
        else:
            self.updateTotalHP()
            return False

    def activatePersonalAttribute(self):
        for i in range(0, len(self.cStatLabelList)):
            self.userCStats[i] *= self.userPersonalAttribute.cStatAMods[i]
        for i in range(0, len(self.oStatLabelList)):
            self.userOStats[i] *= self.userPersonalAttribute.oStatAMods[i]

    def deactivatePersonalAttribute(self):
        for i in range(0, len(self.cStatLabelList)):
            self.userCStats[i] /= self.userPersonalAttribute.cStatAMods[i]
        for i in range(0, len(self.oStatLabelList)):
            self.userOStats[i] /= self.userPersonalAttribute.oStatAMods[i]

    def updateTotalHP(self):
        if self.hPSplit[0] == 0 or self.hPSplit[1] == 0:
            self.userCStats[0] = 0
            return

        total = 0
        for i in range(0, len(self.hPSplit)):
            total += self.hPSplit[i]
        self.userCStats[0] = round(total)

    def changeStamina(self, change):
        self.userCStats[2] -= change

    def getAttacks(self):
        atkList = "| "
        for atk in self.userJob.attacks.keys():
            atkList += atk + " | "
        return atkList

    def getDodges(self):
        dodgeList = "| "
        for dodge in self.userJob.dodges.keys():
            dodgeList += dodge + " | "
        return dodgeList

    def getBlocks(self):
        blockList = "| "
        for block in self.userJob.blocks.keys():
            blockList += block + " | "
        return blockList
