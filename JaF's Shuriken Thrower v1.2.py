# JustanotherFace (JaF) for RE; JaF's Shuriken Thrower
# Original V1.0: 01/31/2023 
# Current Version V1.2 02/02/2023
#
# Obviously you need a ninja belt in your backpack. 
# Initially load that ninja belt up with 10 poisoned shurikens
# Put at least 1 (more suggested) INSURED stack(s) of 10 shurikens in your backpack
#
# When you toggle on either a primary or secondary ability
#   and you are within the range requirements for using Shurikens (3-10 tiles from target)
#   the script will auto throw a shuriken at the last target you attacked. 
# Shurikens have a use reset timer of 5 seconds. After using a shuriken and after 5 seconds pass
#   when you toggle on a primary or secondary it will again throw a shuriken at your target. 
#
# When you use all the charges from your ninja belt the script will reload the belt
#   from the shurikens you have in your backpack. 
# If you run out of shurikens in your backpack the script will stop and alert you 
#   that you are out of shurikens. 


from System.Collections.Generic import List 
belt = 0x2790
backpack = Player.Backpack.Serial
shur = 0x27AC
belt1 = Items.FindByID(belt, -1, backpack)
shurtimer = False
Journal.Clear()
ignore = []

def useshur():
    belt = 0x2790
    backpack = Player.Backpack.Serial
    shur = 0x27AC
    
    Items.FindByID(shur, -1, Player.Backpack.Serial)
    if Player.HasSpecial and Timer.Check("shurtimer") == False:
        
        Ltarget = Target.GetLastAttack( )
        Target.SetLast(Ltarget) 
        Misc.Pause(600)
        Items.UseItemByID(belt,-1)
        if Journal.Search ("no shuriken in your ninja belt"):
            Journal.Clear()
            reload()
        else:
            Target.WaitForTarget(1200,False)
            Target.Last()
            Timer.Create("shurtimer", 5500)
            Misc.Pause(1000)


# Out of Shurikens? Reload            

def reload(): 
    Journal.Clear()
    belt = 0x2790
    backpack = Player.Backpack.Serial
    shur = 0x27AC
    Items.FindByID(shur, -1, Player.Backpack.Serial)

    for shurs in Items.FindBySerial(Player.Backpack.Serial).Contains:
        Misc.Pause(75)
        if shurs.ItemID != (shur):
            ignore.append(shurs.Serial)
        
        elif shurs.ItemID == (shur) and Items.BackpackCount(shur) >= 1 and shurs.Serial not in ignore:
            Journal.Clear()
# Open Ninja Belt Contect and choose load
            Misc.WaitForContext(belt1.Serial, 10000)
            Misc.ContextReply(belt1.Serial, "Load Ninja Belt")
            
# With target cursor from load belt, target shuriken stack
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(shurs.Serial)
            Journal.Clear()
            Misc.Pause(1200)
            useshur()
            break
            
    else: 
        Player.HeadMessage(55, "You are out of Shurikens")
        Stop
            

while True:
    useshur()