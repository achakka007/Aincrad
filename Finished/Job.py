from Labels import Labels
import random


class Job:

    cStatLabels = Labels.cStatLabelList
    oStatLabels = Labels.oStatLabelList

    def __init__(self, jobName="Job", nextJobs=[]):

        self.jobName = jobName
        self.description = "DNE"
        self.nextJobs = ["Fighter"]

        self.cStatBoosts = []  # Array of Doubles
        self.oStatBoosts = []  # Array of Doubles

        for _i in range(0, len(self.cStatLabels)):
            self.cStatBoosts.append(1)
        for _i in range(0, len(self.oStatLabels)):
            self.oStatBoosts.append(1)

        def punch(self):
            print(Labels.userBodyPartLabels)
            target = input("Select target: ")
            accuracy = 70
            if (target == "Head"):
                accuracy -= 40
            if (target == "Body"):
                accuracy += 20
            return {'atkmod': 1, 'target': target, 'accuracy': accuracy, 'cost': 100, 'cooldown': 0, 'rounds passed': 0, 'debuff name': "None", 'debuff effect': "None"}

        def kick(self):
            print(Labels.userBodyPartLabels)
            target = input("Select target: ")
            accuracy = 60
            if (target == "Head"):
                accuracy -= 40
            if (target == "Body"):
                accuracy += 30
            return {'atkmod': 1.2, 'target': target, 'accuracy': accuracy, 'cost': 120, 'cooldown': 0, 'rounds passed': 0, 'debuff name': "None", 'debuff effect': "None"}

        def dodge(self):
            return {'success': (random.randint(1, 100) > 70), 'cost': 75}

        def block(self):  # Cannot use Head or Body!
            target = input("Select what to block with: ")
            while target == "Head" or target == "Body":
                print("Invalid Input")
                target = input("Select what to block with: ")

            return {'target': target, 'damage reduction': 0.2, 'cost': 25}

        self.attacks = {'punch': punch, 'kick': kick}
        self.attackCooldowns = {'punch': 0, 'kick': 0}

        self.dodges = {'dodge': dodge}

        self.blocks = {'block': block}

    def changeCStatBoost(self, statName, num):
        self.cStatBoosts[self.cStatLabels.index(statName)] += num

    def changeOStatBoost(self, statName, num):
        self.oStatBoosts[self.oStatLabels.index(statName)] += num

    def showStatBoosts(self):
        print("Combat Stats:")
        for i in range(0, len(self.cStatLabels)):
            print("{} = {}".format(self.cStatLabels[i], self.cStatBoosts[i]))
        print("\nOther Stats:")
        for i in range(0, len(self.oStatLabels)):
            print("{} = {}".format(self.oStatLabels[i], self.oStatBoosts[i]))

    def changeCStatBoosts(self, lis):
        for pair in lis:
            self.changeCStatBoost(pair[0], pair[1])

    def changeOStatBoosts(self, lis):
        for pair in lis:
            self.changeOStatBoost(pair[0], pair[1])

    def showDescription(self):
        print("Description: {}".format(self.description))
