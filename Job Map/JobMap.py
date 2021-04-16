import random
from JobForMap import *
# from User import *

# Fighter Class
# Branch 1
# LVL 200
SpiritChampion = Job("Spirit Champion")
Rider = Job("Rider")
SwordKing = Job("Sword King")
# LVL 100
ElementalSwordsman = Job("Elemental Swordsman", [SpiritChampion])
IllusionarySwordsman = Job("Illusionary Swordsman")
EnhancerXSwordsman = Job("Enhancer Swordsman")
GrandmasterSwordsman = Job("Grandmaster Swordsman", [Rider, SwordKing])
SwordArtist = Job("Sword Artist")
Breaker = Job("Breaker")
MagicDualSwordsman = Job("Magic Dual Swordsman")
TriSwordsman = Job("Tri Swordsman")
BladeDancer = Job("Blade Dancer")
# LVL 50
MagicSwordsman = Job("Magic Swordsman", [ElementalSwordsman, IllusionarySwordsman, EnhancerXSwordsman])
Swordsmaster = Job("Swordsmaster", [GrandmasterSwordsman, SwordArtist, Breaker])
DualSwordsman = Job("Dual Swordsman", [MagicDualSwordsman, TriSwordsman, BladeDancer])
# LVL 10
Knight = Job("Knight", [MagicSwordsman, Swordsmaster, DualSwordsman])

# Branch 2
# LVL 200
SpatialGuardian = Job("Spatial Guardian")
Frankenstein = Job("Frankenstein")
Valkyrie = Job("Valykrie")
#LVL 100
KickBoxer = Job("Kick Boxer")
ElementalBoxer = Job("Elemental Boxer", [SpatialGuardian])
MasterBoxer = Job("Master Boxer")
Karate = Job("Karate")
ElementalKungfu = Job("Elemental Kungfu")
ComboSeeker = Job("Combo Seeker")
Pirate = Job("Pirate")
Hulk = Job("Hulk", [Frankenstein])
Axeman = Job("Axeman", [Valkyrie])
# LVL 50
Boxer = Job("Boxer", [KickBoxer, ElementalBoxer, MasterBoxer])
Kungfu = Job("Kungfu", [Karate, ElementalKungfu, ComboSeeker])
Beserker = Job("Beserker", [Pirate, Hulk, Axeman])
# LVL 10
MartialArtist = Job("Martial Artist", [Boxer, Kungfu, Beserker])

# Branch 3
# LVL 200
Trickster = Job("Trickster")
GuardianDeity = Job("Guardian Deity")
# LVL 100
ElementalAssassin = Job("Elemental Assassin")
Corroder = Job("Corroder")
Shadow = Job("Shadow", [Trickster])
ElementalNinja = Job("Elemental Ninja")
NinjutsuUser = Job("Ninjutsu User")
YinYangUser = Job("Yin Yang User")
StoneGuardian = Job("StoneGuardian", [GuardianDeity])
WeaponsMaster = Job("WeaponsMaster")
TimeManipulator = Job("TimeManipulator")
# LVL 50
PoisonUser = Job("Poison User", [ElementalAssassin, Corroder, Shadow])
Ninja = Job("Ninja", [ElementalNinja, NinjutsuUser, YinYangUser])
DualWielderXAssassin = Job("Dual Wielder Assassin", [StoneGuardian, WeaponsMaster, TimeManipulator])
# LVL 10
Assassin = Job("Assassin", [PoisonUser, Ninja, DualWielderXAssassin])
# LVL 1
Fighter = Job("Fighter", [Knight, MartialArtist, Assassin])

# Mage Class
# Branch 1
# LVL 200
Witch = Job("Witch")
Vampire = Job("Vampire")
CloneCreator = Job("Clone Creator")
# LVL 100
Archmage = Job("Archmage")
BlackMagician = Job("Black Magician", [Witch, Vampire])
BloodMagician = Job("Blood Magician", [CloneCreator])
MasterOfTwoXMage = Job("Master Of Two - Mage")
Beyonder = Job("Beyonder")
# LVL 50
Grandmage = Job("Grandmage", [Archmage])
RitualMaster = Job("Ritual Master", [BlackMagician, BloodMagician])
MasterOfOneXMage = Job("Master Of One - Mage", [MasterOfTwoXMage, Beyonder])
# LVL 10
ElementalMage = Job("ElementalMage", [Grandmage, RitualMaster, MasterOfOneXMage])

# Branch 2
# LVL 200
MasterPhysician = Job("Master Physician")
# LVL 100
GreatHealer = Job("Great Healer")
MasterHealer = Job("Master Healer")
Physician = Job("Physician", [MasterPhysician])
TribalGuardian = Job("Tribal Guardian")
SpiritGuardian = Job("Spirit Guardian")
MasterManipulator = Job("Master Manipulator")
TimeGod = Job("Time God")
# LVL 50
Healer = Job("Healer", [GreatHealer, MasterHealer, Physician])
Guardian = Job("Guardian", [TribalGuardian, SpiritGuardian])
Manipulator = Job("Manipulator", [MasterManipulator, TimeGod])
# LVL 10
SupportMage = Job("Support Mage", [Healer, Guardian, Manipulator])

# Branch 3
# LVL 200
SpiritRider = Job("Spirit Rider")
# LVL 100
SpiritBeastTamer = Job("SpiritBeastTamer", [SpiritRider])
SpiritBeastSlaver = Job("Spirit Beast Slaver")
FortressKing = Job("Fortress King")
SwarmQueen = Job("Swarm Queen")
ZombieHoarder = Job("Zombie Hoarder")
Reviver = Job("Reviver")
# LVL 50
SpiritBeastSummoner = Job("Spirit Beast Summoner", [SpiritBeastTamer, SpiritBeastSlaver])
MachineGod = Job("Machine God", [FortressKing, SwarmQueen])
UndeadSummoner = Job("Undead Summoner", [ZombieHoarder, Reviver])
# LVL 10
Summoner = Job("Summoner", [SpiritBeastSummoner, MachineGod, UndeadSummoner])
# LVL 1
Mage = Job("Mage", [ElementalMage, SupportMage, Summoner])

# Spearman Class
# Branch 1
# LVL 200
MasterOfOneHundredSpears = Job("Master Of One Hundred Spears")
# LVL 100
MasterOfOneXSpearman = Job("Master Of One X Spearman")
JackOfAllTradesXSpearman = Job("Jack Of All Trades X Spearman")
PastPiercer = Job("Past Piercer")
FutureSlicer = Job("Future Slicer")
MasterEnhancerXSpearman = Job("MasterEnhancer X Spearman")
GuardianMonkXSpearman = Job("Guardian Monk - Spearman", [MasterOfOneHundredSpears])
SpiritUserXSpearman = Job("SpiritUser - Spearman")
# LVL 50
ElementalSpearman = Job("Elemental Spearman", [MasterOfOneXSpearman, JackOfAllTradesXSpearman])
IllusionarySpearman = Job("Illusionary Spearman", [PastPiercer, FutureSlicer])
EnhancerXSpearman = Job("Enhancer X Spearman", [MasterEnhancerXSpearman])
HolySpearman = Job("Holy Spearman", [GuardianMonkXSpearman, SpiritUserXSpearman]) 
# LVL 10
MagicSpearman = Job("Magic Spearman", [ElementalSpearman, IllusionarySpearman, EnhancerXSpearman, HolySpearman])
# Branch 2
# LVL 200

# LVL 100
GrandmasterJouster = Job("Grandmaster Jouster")
MythicalJouster = Job("Mythical Jouster")
BloodGryphonJouster = Job("Blood Gryphon Jouster")

# LVL 50
DragonJouster = Job("Dragon Jouster")
MasterJouster = Job("Master Jouster", [GrandmasterJouster])
GryphonJouster = Job("Gryphon Jouster", [MythicalJouster, BloodGryphonJouster])

# LVL 10
Jouster = Job("Jouster", [DragonJouster, MasterJouster, GryphonJouster])
# Branch 3
# LVL 200
SpearGod = Job("Spear God")
# LVL 100
ElementalDualSpearman = Job("Elemental Dual Spearman")
RicochetSpecialistXSpearman = Job("Ricochet Specialist X Spearman")
MechanizedSpear = Job("Mechanized Spear")
MechanizedSpearman = Job("Mechanized Spearman")
SpearKing = Job("Spear King", [SpearGod])

# LVL 50
DualSpearman = Job("Dual Spearman", [ElementalDualSpearman, RicochetSpecialistXSpearman])
CyborgSpearman = Job("Cyborg Spearman", [MechanizedSpear, MechanizedSpearman])
GrandmasterSpearman = Job("Grandmaster Spearman", [SpearKing])

# LVL 10
MasterSpearman = Job("Master Spearman", [DualSpearman, CyborgSpearman, GrandmasterSpearman])
# LVL 1
Spearman = Job("Spearman", [MagicSpearman, Jouster, MasterSpearman])

# Alchemist Class
# Branch 1
# LVL 200

# LVL 100
MagicBuffSpecialist = Job("Magic Buff Specialist")
PlantBuffSpecialist = Job("Plant Buff Specialist") 
AnimalBuffSpecialist = Job("Animal Buff Specialist")
MagicDebuffSpecialist = Job("Magic Debuff Specialist")
PlantDebuffSpecialist = Job("Plant Debuff Specialist")
AnimalDebuffSpecialist = Job("Animal Debuff Specialist")

# LVL 50
BuffSpecialist = Job("Buff Specialist", [MagicBuffSpecialist, PlantBuffSpecialist, AnimalBuffSpecialist])
DebuffSpecialist = Job("Debuff Specialist", [MagicDebuffSpecialist, PlantDebuffSpecialist, AnimalDebuffSpecialist])

# LVL 10
PotionsMaster = Job("Potions Master", [BuffSpecialist, DebuffSpecialist])
# Branch 2
# LVL 200
ChimeraProfessor = Job("Chimera Professor")
# LVL 100
EliteConverter = Job("Elite Converter")
LivingTransmuter = Job("Living Transmuter", [ChimeraProfessor])
GrandRitualMaster = Job("Grand Ritual Master")
RitualSpecialist = Job("Ritual Specialist")

# LVL 50
COnversionSpecialist = Job("COnversion Specialist", [EliteConverter, LivingTransmuter])
RitualMaster = Job("Ritual Master", [GrandRitualMaster, RitualSpecialist])

# LVL 10
AlchemyMage = Job("Alchemy Mage", [COnversionSpecialist, RitualMaster])
# Branch 3
# LVL 200
# LVL 100
ChaosMage = Job("Chaos Mage")
GrandBlackMagician = Job("Grand Black Magician")
BeserkAlchemist = Job("Beserk Alchemist")
SacrificeOverseer = Job("Sacrifice Overseer")

# LVL 50
BlackMagician = Job("Black Magician", [ChaosMage, GrandBlackMagician])
BloodAlchemist = Job("Blood Alchemist", [BeserkAlchemist, SacrificeOverseer])

# LVL 10
DarkAlchemist = Job("Dark Alchemist", [BlackMagician, BloodAlchemist])
# LVL 1
Alchemist = Job("Alchemist", [PotionsMaster, AlchemyMage, DarkAlchemist])

# Archer Class
# Branch 1
# LVL 200
Ranger = Job("Ranger")
Hunter = Job("Hunter")

# LVL 100
MasterOfOneXArcher = Job("Master Of One X Archer")
SpatialManipulator = Job("Spatial Manipulator")
Scout = Job("Scout", [Ranger])
Dealer = Job("Dealer", [Hunter])
BowMaster = Job("Bow Master")
QuadLauncher = Job("Quad Launcher")

# LVL 50
ElementalArcher = Job("Elemental Archer", [MasterOfOneXArcher, SpatialManipulator])
SpecializedArcher = Job("Specialized Archer", [Scout, Dealer])
GrandArcher = Job("Grand Archer", [BowMaster, QuadLauncher])

# LVL 10
MasterArcher = Job("Master Archer", [ElementalArcher, SpecializedArcher, GrandArcher])
# Branch 2
# LVL 200
# LVL 100
MasterSniper = Job("Master Sniper")
MagicSniper = Job("Magic Sniper")
DualPistols = Job("Dual Pistols")
GunMage = Job("Gun Mage")
MissileMarauder = Job("Missile Marauder")
ExpertGunner = Job("Expert Gunner")

# LVL 50
Sniper = Job("Sniper", [MasterSniper, MagicSniper])
MagicPistolUser = Job("Magic Pistol User", [DualPistols, GunMage])
Gunner = Job("Gunner", [MissileMarauder, ExpertGunner])

# LVL 10
GunLord = Job("Gun Lord", [Sniper, MagicPistolUser, Gunner])
# Branch 3
# LVL 200
# LVL 100
Destroyer = Job("Destroyer")
OneWithNature = Job("One With Nature")
MagicPlantExpert = Job("Magic Plant Expert")
SlingshotMage = Job("Slingshot Mage")
SlingshotDeity = Job("Slingshot Deity")

# LVL 50
ExplosiveExpert = Job("Explosive Expert", [Destroyer])
PlantExpert = Job("Plant Expert", [OneWithNature, MagicPlantExpert])
MagicExpertXSlingshot = Job("Magic Expert X Slingshot", [SlingshotMage, SlingshotDeity])

# LVL 10
SlingshotUser = Job("Slingshot User", [ExplosiveExpert, PlantExpert, MagicExpertXSlingshot])
# LVL 1
Archer = Job("Archer", [MasterArcher, GunLord, SlingshotUser])

#Class Creator Code

a = [["MasterOfOneXArcher", "SpatialManipulator"], "ElementalArcher", ["Scout", "Dealer"], "SpcializedArcher", ["Bow Master", "Quad Launcher"], "GrandArcher", "MasterArcher"]
b = [["MasterSniper", "MagicSniper"], "Sniper", ["DualPistols", "GunMage"], "MagicPistolUser", ["Missile Marauder", "Expert Gunner"], "Gunner", "GunLord"]
c = [["Destroyer"], "ExplosiveExpert", ["OneWithNature", "MagicPlantExpert"], "PlantExpert", ["SlingshotMage", "SlingshotDeity"], "MagicExpertXSlingshot", "SlingshotUser"]
d = "Archer"

print("# {} Class".format(d))
for r in range(0,3):
    if r == 0: 
        x = a
    if r == 1: 
        x = b
    if r == 2: 
        x = c
    print("# Branch {}".format(r+1))
    print("# LVL 200")

    print("# LVL 100")
    for i in range(0,len(x)-2,2):
        for j in range(0,len(x[i])):
            print("{} = Job(\"{}\")".format(x[i][j],x[i][j]))
    print()
    
    print("# LVL 50")
    for i in range(0,len(x)-1,2):
        if (len(x[i]) == 4):
            print("{} = Job(\"{}\", [{}, {}, {}, {}])".format(x[i+1], x[i+1], x[i][0], x[i][1], x[i][2], x[i][3]))
        elif (len(x[i]) == 3):
            print("{} = Job(\"{}\", [{}, {}, {}])".format(x[i+1], x[i+1], x[i][0], x[i][1], x[i][2]))
        elif (len(x[i]) == 2):
            print("{} = Job(\"{}\", [{}, {}])".format(x[i+1], x[i+1], x[i][0], x[i][1]))
        elif (len(x[i]) == 1):
            print("{} = Job(\"{}\", [{}])".format(x[i+1], x[i+1], x[i][0]))
        else:
            pass
    print()

    print("# LVL 10")
    if len(x) == 9:
        print("{} = Job(\"{}\", [{}, {}, {}, {}])".format(x[8], x[8], x[1], x[3], x[5], x[7]))
    elif len(x) == 7:
        print("{} = Job(\"{}\", [{}, {}, {}])".format(x[6], x[6], x[1], x[3], x[5]))
    elif len(x) == 5:
        print("{} = Job(\"{}\", [{}, {}])".format(x[4], x[4], x[1], x[3]))
    else:
        pass

print("# LVL 1")
print("{} = Job(\"{}\", [{}, {}, {}])".format(d, d, a[-1], b[-1], c[-1]))



