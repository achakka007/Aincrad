from PersonalAttribute import PersonalAttribute

TrailBlazer = PersonalAttribute("Trail Blazer", """    As someone who dives head first into challenges 
    you have been granted a 120{} cStat boost at the 
    beginning of combat. The boost will end after 5 minutes.""".format("%"))
_i = 0
for _cStat in TrailBlazer.cStatLabels:
    if _i >= 3:
        TrailBlazer.changeCStatAMod(_cStat, 0.2) # Further Work Required - The boost will decrease by 4{} every minute.
    _i+=1
def _trailBlazerIsActive(**kwargs):
    round = kwargs.get('Round')
    if(round == 1):
        return True
    return False
def _trailBlazerIsDeActive(**kwargs):
    round = kwargs.get('Round')
    if(round == 5):
        return True
    return False
TrailBlazer.isActive = _trailBlazerIsActive
TrailBlazer.isDeActive = _trailBlazerIsDeActive

AbsoluteLuck = PersonalAttribute("Absolute Luck", """    You have been granted a 200{} luck boost by the 
    system in recognition of your amazing luck.""".format("%"))
AbsoluteLuck.changeOStatPMod("Luck", 1)

Sage = PersonalAttribute("Sage", """    You have been granted a 200{} intelligence boost 
    by the system in recognition of your amazing wisdom.""".format("%"))
Sage.changeCStatPMod("Intelligence", 1)


Genius = PersonalAttribute("Genius", """    You have been granted a 110{} EXP boost 
    by the system in recognition of your amazing talent.""".format("%"))
Genius.changeOStatPMod("Experience Accumulation", 0.1)


Idol = PersonalAttribute("Idol", """    You have been granted a 200{} charisma boost 
    by the system in recognition of your amazing talent.""".format("%"))
Idol.changeOStatPMod("Charisma", 1)

Phantom = PersonalAttribute("Phantom", """    You have been granted a 200{} stealth boost 
    by the system in recognition of your ability to stay hidden.""".format("%"))
Phantom.changeCStatPMod("Stealth", 1)

SilverTongue = PersonalAttribute("Silver Tongue", """    You have been granted a 150{} charisma and 
    bargaining boost by the system in recognition 
    of your ability to communicate.""".format("%"))
SilverTongue.changeOStatPMod("Charisma", 0.5)
SilverTongue.changeOStatPMod("Bargaining", 0.5)

FastOnYourFeet = PersonalAttribute("Fast On Your Feet", """    You have been granted a 150{} speed boost 
    by the system in recognition of your ability to move quickly.""".format("%"))
FastOnYourFeet.changeCStatPMod("Speed", 0.5)

Clutch = PersonalAttribute("Clutch", """    You have been granted a 150{} all stat boost 
    by the system when HP < 15{} in recognition of your ability to move quickly.""".format("%","%"))
def _clutchIsActive(OrigUser = None, CurrUser = None, **kwargs):
    if(CurrUser.getHealth() <= (OrigUser.getHealth() * 15 / 100)):
        return True
    return False
def _clutchIsDeActive(OrigUser = None, CurrUser = None, **kwargs):
    return False
_i = 0
for _cStat in Clutch.cStatLabels:
    if _i >= 3:
        Clutch.changeCStatAMod(_cStat, 0.5)
    _i+=1
Clutch.isActive = _clutchIsActive
Clutch.isDeActive = _clutchIsDeActive
