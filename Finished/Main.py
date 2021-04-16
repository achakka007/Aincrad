import random
from User import User
from Job import Job
import os

# from Chestplate import *
# from Helmet import *
# from LeftBoot import *
# from RightBoot import *
# from LeftGauntlet import *
# from RightGauntlet import *


def main():
    a = User(Type="NPC", Name="A", Job="Fighter")
    b = User(Type="NPC", Name="B", Job="Tank")

    # a = User(Type = "Real")
    # b = User(Type = "Real")

    # a.equipArmor("Hide Chestplate")
    # b.equipArmor("Hide Chestplate")

    a.showUser()
    b.showUser()

    # combat(a, b, showDmg=True)
    combatV2(a, b)


def combatV2(user1, user2):
    u1 = User(Type="Copy", User=user1)
    u2 = User(Type="Copy", User=user2)
    print("Combat has begun between {}({}) and {}({})".format(
        u1.username, u1.userJob.jobName, u2.username, u2.userJob.jobName))
    round = 1
    print("Starting Health: ")
    print("{}: {}".format(u1.username, u1.getHealth()))
    print("{}: {}".format(u2.username, u2.getHealth()))
    input("Begin Combat?")
    os.system('clear')

    beforeActivation1 = True
    beforeDeactivation1 = True
    beforeActivation2 = True
    beforeDeactivation2 = True

    u1AtkHistory = setAtkHistory(u1)
    u2AtkHistory = setAtkHistory(u2)

    while (u1.getHealth() > 0 and u2.getHealth() > 0):
        # Personal Attribute Activation
        if u1.userPersonalAttribute.isActive(OrigUser=user1, CurrUser=u1, Round=round) and beforeActivation1:
            u1.activatePersonalAttribute()
            print("{} has activated their personal attribute: {}".format(
                u1.username, u1.userPersonalAttribute.name))
            beforeActivation1 = False
        if u2.userPersonalAttribute.isActive(OrigUser=user2, CurrUser=u2, Round=round) and beforeActivation2:
            u2.activatePersonalAttribute()
            print("{} has activated their personal attribute: {}".format(
                u2.username, u2.userPersonalAttribute.name))
            beforeActivation2 = False

        # COMBAT
        # USER 1 INPUT
        print("ROUND:   {}".format(round))
        combatantDetails(u1)
        userChoice01 = input("{}: Choose Attack, Dodge or Block: ".format(u1.username))
        print()

        if userChoice01 == "Attack":
            print("Attacks: Cooldowns => {}".format(
                waitTimes(u1, u1AtkHistory, round)))
            userChoice1 = input("Choose attack: ").lower()
            if userChoice1 in u1.userJob.attacks:  # Attack Type Calculations
                # punch()
                atkFunc1 = u1.userJob.attacks[userChoice1]
                # Array of Attack Details
                atkType1 = atkFunc1(u1.userJob)
                atkType1['rounds passed'] = round - u1AtkHistory[userChoice1] - 1
                # Update History
                u1AtkHistory[userChoice1] = round
            else:
                break
        elif userChoice01 == "Dodge":
            print("Dodges: {}".format(u1.getDodges()))
            userChoice1 = input("Choose dodge: ")
            if userChoice1 in u1.userJob.dodges:
                dodgeFunc1 = u1.userJob.dodges[userChoice1]       # dodge()
                # Array of Dodge Details
                dodgeType1 = dodgeFunc1(u1.userJob)
                # boolean for dodge
                dodgeSucceeded1 = dodgeType1['success']
            else:
                break
        elif userChoice01 == "Block":
            print("Blocks: {}".format(u1.getBlocks()))
            userChoice1 = input("Choose block: ")
            if userChoice1 in u1.userJob.blocks:
                blockFunc1 = u1.userJob.blocks[userChoice1]        # block()
                # Array of Block Details
                blockType1 = blockFunc1(u1.userJob)
            else:
                break
        else:
            break
        os.system('clear')

        # USER 2 INPUT
        print("ROUND:   {}".format(round))
        combatantDetails(u2)
        userChoice02 = input(
            "{}: Choose Attack, Dodge or Block: ".format(u2.username))
        print()

        if userChoice02 == "Attack":
            print("Attacks: Cooldowns => {}".format(
                waitTimes(u2, u2AtkHistory, round)))
            userChoice2 = input("Choose attack: ").lower()
            if userChoice2 in u2.userJob.attacks:
                atkFunc2 = u2.userJob.attacks[userChoice2]
                atkType2 = atkFunc2(u2.userJob)
                atkType2['rounds passed'] = round - u2AtkHistory[userChoice2] - 1
                u2AtkHistory[userChoice2] = round
            else:
                break
        elif userChoice02 == "Dodge":
            print("Dodges: {}".format(u2.getDodges()))
            userChoice2 = input("Choose dodge: ")
            if userChoice2 in u2.userJob.dodges:
                dodgeFunc2 = u2.userJob.dodges[userChoice2]
                dodgeType2 = dodgeFunc2(u2.userJob)
                dodgeSucceeded2 = dodgeType2['success']
            else:
                break
        elif userChoice02 == "Block":
            print("Blocks: {}".format(u2.getBlocks()))
            userChoice2 = input("Choose block: ")
            if userChoice2 in u2.userJob.blocks:
                blockFunc2 = u2.userJob.blocks[userChoice2]
                blockType2 = blockFunc2(u2.userJob)
            else:
                break
        else:
            break
        os.system('clear')

        # Dodge, Block, Attack Combinations
        if userChoice01 == "Attack" and userChoice02 == "Attack":
            attackAttack(u1, u2, atkType1, atkType2)
        elif userChoice01 == "Dodge" and userChoice02 == "Dodge":
            DodgeDodge(u1, u2, dodgeType1, dodgeType2)
        elif userChoice01 == "Block" and userChoice02 == "Block":
            BlockBlock(u1, u2, blockType1, blockType2)
        elif userChoice01 == "Attack" and userChoice02 == "Dodge":
            attackDodge(u1, u2, atkType1, dodgeType2)
        elif userChoice01 == "Dodge" and userChoice02 == "Attack":
            attackDodge(u2, u1, atkType2, dodgeType1)
        elif userChoice01 == "Attack" and userChoice02 == "Block":
            attackBlock(u1, u2, atkType1, blockType2)
        elif userChoice01 == "Block" and userChoice02 == "Attack":
            attackBlock(u2, u1, atkType2, blockType1)
        elif userChoice01 == "Block" and userChoice02 == "Dodge":
            BlockDodge(u1, u2, atkType1, blockType2)
        elif userChoice01 == "Dodge" and userChoice02 == "Block":
            BlockDodge(u2, u1, atkType2, blockType1)
        else:
            break

        # Personal Attribute Deactivation
        if u1.userPersonalAttribute.isDeActive(OrigUser=user1, CurrUser=u1, Round=round) and beforeDeactivation1 and not beforeActivation1:
            u1.deactivatePersonalAttribute()
            print("{} has deactivated their personal attribute: {}".format(
                u1.username, u1.userPersonalAttribute.name))
            beforeDeactivation1 = False
        if u2.userPersonalAttribute.isDeActive(OrigUser=user2, CurrUser=u2, Round=round) and beforeDeactivation2 and not beforeActivation2:
            u2.deactivatePersonalAttribute()
            print("{} has deactivated their personal attribute: {}".format(
                u2.username, u2.userPersonalAttribute.name))
            beforeDeactivation2 = False

        print()
        print("<<ROUND RESULTS>>")
        print("U1 HP = {}".format(round(u1.getHealth())))
        print("U2 HP = {}".format(round(u2.getHealth())))
        print("<<<<<<<--->>>>>>>")
        input("Continue?")
        os.system('clear')

        round += 1

    # Decide Winner
    if u1.getHealth() <= 0 and u2.getHealth() <= 0:
        print("Both players have died!")
    elif u1.getHealth() <= 0:
        print("{} wins!".format(u2.username))
    elif u2.getHealth() <= 0:
        print("{} wins!".format(u1.username))
    else:
        print("Error")

    print()
    print("U1 FINAL HP = {}".format(u1.hPSplit))
    print("U2 FINAL HP = {}".format(u2.hPSplit))


def combat(user1, user2, showDmg=True):  # Make Copies at Beginning
    u1 = User(Type="Copy", User=user1)
    u2 = User(Type="Copy", User=user2)
    print("Combat has begun between {}({}) and {}({})".format(
        u1.username, u1.userJob.jobName, u2.username, u2.userJob.jobName))
    round = 1
    print("Starting Health: ")
    print("{}: {}".format(u1.username, u1.getHealth()))
    print("{}: {}".format(u2.username, u2.getHealth()))

    beforeActivation1 = True
    beforeDeactivation1 = True
    beforeActivation2 = True
    beforeDeactivation2 = True

    while (u1.getHealth() > 0 and u2.getHealth() > 0):
        print("Round: {}".format(round))

        # Personal Attribute Activation
        if u1.userPersonalAttribute.isActive(OrigUser=user1, CurrUser=u1, Round=round) and beforeActivation1:
            u1.activatePersonalAttribute()
            print("{} has activated their personal attribute: {}".format(
                u1.username, u1.userPersonalAttribute.name))
            beforeActivation1 = False
        if u2.userPersonalAttribute.isActive(OrigUser=user2, CurrUser=u2, Round=round) and beforeActivation2:
            u2.activatePersonalAttribute()
            print("{} has activated their personal attribute: {}".format(
                u2.username, u2.userPersonalAttribute.name))
            beforeActivation2 = False

        # COMBAT
        # USER 1
        userChoice = input("{}: Choose attack: ".format(u1.username))
        print("{}: ".format(u1.username), end='')
        if userChoice in u1.userJob.attacks:  # Attack Type Calculations
            atkFunc = u1.userJob.attacks[userChoice]
            atkType = atkFunc(u1.userJob)
            target = selectTarget(u2, atkType['target'])
        else:
            break

        dmg = u1.getAttack() * atkType['atkmod'] - u2.getDefense(target)
        if dmg < 0:
            u2.changeHealth(0, target)
            if showDmg:
                print("{} does {} damage to {}'s {}".format(
                    u1.username, 0, u2.username, target))
        else:
            # Accuracy Check
            if (random.randint(0, 100) < atkType['accuracy']):
                if showDmg:
                    print("{} does {} damage to {}'s {}".format(
                        u1.username, dmg, u2.username, target))
                # Damage Dealt && Check if body part is disabled.
                if u2.changeHealth(dmg * -1, target):
                    print("{} has lost their {}".format(u2.username, target))
            else:
                if showDmg:
                    print("{} misses the attack at {}'s {}".format(
                        u1.username, u2.username, target))

        # USER 2
        userChoice = input("{}: Choose attack: ".format(u2.username))
        print("{}: ".format(u2.username), end='')
        if userChoice in u2.userJob.attacks:  # Attack Type Calculations
            atkFunc = u2.userJob.attacks[userChoice]
            atkType = atkFunc(u2.userJob)
            target = selectTarget(u1, atkType['target'])
        else:
            break

        dmg = u2.getAttack() * atkType['atkmod'] - u1.getDefense(target)
        if dmg < 0:
            u1.changeHealth(0, target)
            if showDmg:
                print("{} does {} damage to {}'s {}".format(
                    u2.username, 0, u1.username, target))
        else:
            # Accuracy Check
            if (random.randint(0, 100) < atkType['accuracy']):
                if showDmg:
                    print("{} does {} damage to {}'s {}".format(
                        u2.username, dmg, u1.username, target))
                # Damage Dealt && Check if body part is disabled.
                if u1.changeHealth(dmg * -1, target):
                    print("{} has lost their {}".format(u1.username, target))
            else:
                if showDmg:
                    print("{} misses the attack at {}'s {}".format(
                        u2.username, u1.username, target))

        # Personal Attribute Deactivation
        if u1.userPersonalAttribute.isDeActive(OrigUser=user1, CurrUser=u1, Round=round) and beforeDeactivation1 and not beforeActivation1:
            u1.deactivatePersonalAttribute()
            print("{} has deactivated their personal attribute: {}".format(
                u1.username, u1.userPersonalAttribute.name))
            beforeDeactivation1 = False
        if u2.userPersonalAttribute.isDeActive(OrigUser=user2, CurrUser=u2, Round=round) and beforeDeactivation2 and not beforeActivation2:
            u2.deactivatePersonalAttribute()
            print("{} has deactivated their personal attribute: {}".format(
                u2.username, u2.userPersonalAttribute.name))
            beforeDeactivation2 = False

        round += 1

    # Decide Winner
    if u1.getHealth() <= 0 and u2.getHealth() <= 0:
        print("Both players have died!")
    elif u1.getHealth() <= 0:
        print("{} wins!".format(u2.username))
    elif u2.getHealth() <= 0:
        print("{} wins!".format(u1.username))
    else:
        print("Error")

    print("U1 HP = {}".format(u1.hPSplit))
    print("U2 HP = {}".format(u2.hPSplit))

# COMBAT HELPERS


def selectTarget(user, bodyPart):
    userBodyPartLabels = ["Head", "Body", "Right Hand",
                          "Left Hand", "Right Leg", "Left Leg"]
    target = userBodyPartLabels[random.randint(0, len(userBodyPartLabels)-1)]
    if(bodyPart is None):
        while(user.getBodyPartHealth(target) < 0):
            target = userBodyPartLabels[random.randint(
                0, len(userBodyPartLabels)-1)]
    else:
        target = bodyPart
    return target

# COMBAT 2 HELPERS


def attack(uA, uR, atkType, success=True, dmgModifier=1):
    uA.changeStamina(atkType['cost'])
    if (not success):
        return

    dmg1 = round(uA.getAttack() * atkType['atkmod'] - uR.getDefense(atkType['target'])) * dmgModifier
    if dmg1 < 0 or uA.getStamina() < 0 or atkType['rounds passed'] < atkType['cooldown']:
        print("{} has failed to attack {}".format(uA.username, uR.username))
        uR.changeHealth(0, atkType['target'])
    else:
        if (random.randint(0, 100) < atkType['accuracy']):  # Accuracy Check
            # Damage Dealt && Check if body part is disabled.
            if uR.changeHealth(dmg1 * -1, atkType['target']):
                print("{} has lost their {}".format(uR.username, atkType['target']))
            print("{} has done {} dmg to {}".format(uA.username, dmg1, uR.username))
        else:
            print("{} missed".format(uA.username))


def attackAttack(u1, u2, atkType1, atkType2):
    print("Both players have attacked each other")
    # USER 1 Attack
    attack(u1, u2, atkType1)

    # USER 2 Attack
    attack(u2, u1, atkType2)


def attackDodge(uAttacker, uDodger, atkType, dodgeType):
    uDodger.changeStamina(dodgeType['cost'])
    if dodgeType['success'] and uDodger.getStamina() > 0:
        print("{} has managed to evade {}'s attack".format(uDodger.username, uAttacker.username))
        attack(uAttacker, uDodger, atkType, True)
    else:
        print("{} has failed to evade {}'s attack".format(uDodger.username, uAttacker.username))
        attack(uAttacker, uDodger, atkType, False)


def attackBlock(uAttacker, uBlocker, atkType, blockType):
    uBlocker.changeStamina(blockType['cost'])

    if (uBlocker.getStamina() > 0):
        atkType['target'] = blockType['target']
        print("{} has blocked {}'s attack with their {}".format(uBlocker.username, uAttacker.username, blockType['target']))
        attack(uAttacker, uBlocker, atkType, True, blockType['damage reduction'])
    else:
        print("{} failed to block {}'s attack with their {}".format(uBlocker.username, uAttacker.username, blockType['target']))
        attack(uAttacker, uBlocker, atkType, True)


def BlockDodge(uBlocker, uDodger, blockType, dodgeType):
    uBlocker.changeStamina(blockType['cost'])
    uDodger.changeStamina(dodgeType['cost'])
    print("Both players make defensive maneuvers")


def BlockBlock(u1, u2, blockType1, blockType2):
    u1.changeStamina(blockType1['cost'])
    u2.changeStamina(blockType2['cost'])
    print("Both players brace for impact")


def DodgeDodge(u1, u2, dodgeType1, dodgeType2):
    u1.changeStamina(dodgeType1['cost'])
    u2.changeStamina(dodgeType2['cost'])
    print("Both players have attempted evasive maneuvers")


def setAtkHistory(user):
    atkHistory = {}
    for key in user.userJob.attacks.keys():
        atkHistory[key] = 0
    return atkHistory


# AESTHETICS

def combatantDetails(user):
    print()
    print("User:    {}".format(user.username))
    print("Health:  {}".format(round(user.getHealth())))
    print("Stamina: {}".format(round(user.getStamina())))
    print()


def waitTimes(user, atkHistory, round):
    waitTimes = {}
    for key, value in atkHistory.items():
        waitTime = user.userJob.attackCooldowns[key] - (round - value - 1)
        waitTimes[key] = waitTime if waitTime > 0 else 0

    return waitTimes


if __name__ == "__main__":
    main()
