
def write(parent,children,grandchildren = None):
    _i = 0
    for child in children:
        print("class {}({}):".format(child,parent))
        print("    def __init__(self):")
        print("        super().__init__()")
        print("        self.jobName = \"{}\"".format(child))
        print("        self.description = \"\"")
        if grandchildren is not None:
            print("        self.nextJobs = {}".format(grandchildren[_i]))
        else:
            print("        self.nextJobs = []")
        print("        self.changeCStatBoosts([")
        print("        (\"Strength\", 0.1),")
        print("        (\"Speed\", 0.2),")
        print("        (\"Stamina\", 0.5),")
        print("        (\"HP\", 0.5),")
        print("        (\"Medical Expertise\", 0.2)") # Add Recovery?
        print("        ])")
        _i+=1
       

x = ["Healer", "Doctor"]

x0 = ["GrandHealer", "ElementalHealer", "BlackHealer"]
x1 = ["Surgeon", "Psychologist", "MasterDoctor"]
# x2 = ["ExplosiveExpert", "PlantExpert", "MagicExpert"]

x00 = ["HolyPriest", "DragonHealer"]
x01 = ["GarndElementalHealer", "MasterOfOneXHealer"]
x02 = ["Resurructionist", "BloodHealer"]

x10 = ["BattleSurgeon", "MasterSurgeon"]
x11 = ["ChiefPsychologist", "Neurosurgeon"]
x12 = ["MasterPhysician", "CyborgSpecialist"]

# x20 = ["Destroyer"]
# x21 = ["OneWithNature", "MagicPlantExpert"]
# x22 = ["SlingshotMage", "SlingshotDeity"]

write("Medic", x, [x0, x1])

write(x[0], x0, [x00,x01,x02])
write(x[1], x1, [x10,x11,x12])
# write(x[2], x2, [x20,x21,x22])

write(x0[0], x00)
write(x0[1], x01)
write(x0[2], x02)
print()
write(x1[0], x10)
write(x1[1], x11)
write(x1[2], x12)
# print()
# write(x2[0], x20)
# write(x2[1], x21)
# write(x2[2], x22)

'''
write("SpiritBeastSummoner", ["SpiritBeastTamer", "SpiritBeastSlaver"])
write("MachineGod", ["FortressKing", "SwarmQueen"])
write("UndeadSummoner", ["ZombieHoarder", "Reviver"])

print()
write("SpiritBeastTamer", ["SpiritRider"])
'''
