# JustanotherFace (JaF) 3rd script for RE; JaF's Smoke Bomb Crafter
# Original V1.0: 09/24/2022 
#
# NOTICE and Thank you: The core of this script was Frank Castle's Enchanted Apple Crafter
# I simply modified an awesome script created by Frank to make it craft Smoke Bombs instead. 
# I also added a few tweaks on top of Frank's original script. 

#You need a secure container with plenty of eggs, ginseng, and iron ingots
#You also need one player made tinker tool in your backpack
#You must have GM Alchemy and Tinkering
#
#WARNING! This will make smoke bombs until you run out of one of the supplies.

from System.Collections.Generic import List

supplyChest = Target.PromptTarget('Target your resource chest')
Misc.Pause(100)
Items.UseItem(supplyChest)
Misc.Pause(1100)

Player.UseSkill('Hiding')
Misc.Pause(11000)

def checkSupplies():
    if Items.BackpackCount(0x09B5,0x0000) < 1: #eggs
        geteggs()
    if Items.BackpackCount(0x0F85,0x0000) < 3: #ginseng
        getginseng()
    Misc.Pause(200)    

def checkTools():        
    if Items.BackpackCount(0x1EB9,-1) < 2: #tinker tools
        makeTinker()
    if Items.BackpackCount(0x0E9B,-1) < 1: #mortar and pestal
        makemortar()
    Misc.Pause(200)
    
def makeTinker():
    if Items.BackpackCount(0x1BF2,-1) < 10:
        sIngot = Items.FindByID(0x1BF2,-1,supplyChest)
        Misc.Pause(200)
        Items.Move(sIngot,Player.Backpack.Serial,10)
        Misc.Pause(1200)
    Items.UseItemByID(0x1EB9,-1)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 11)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 0)
    Misc.Pause(1100)
    if Items.BackpackCount(0x1EB9,-1) < 3:
        makeTinker()
        
def makemortar():
    if Items.BackpackCount(0x1BF2,-1) < 10:
        sIngot = Items.FindByID(0x1BF2,-1,supplyChest)
        Misc.Pause(200)
        Items.Move(sIngot,Player.Backpack.Serial,10)
        Misc.Pause(1200)
    Items.UseItemByID(0x1EB9,-1)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 9)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 0)
    Misc.Pause(200)
    if Items.BackpackCount(0x0E9B,-1) < 10:
        makemortar()
        
def geteggs():
    seggs = Items.FindByID(0x09B5,0x0000,supplyChest)
    Misc.Pause(200)
    count = Items.ContainerCount(supplyChest,0x09B5,0x0000)
    if count > 0:
        Items.Move(seggs,Player.Backpack.Serial,50)
        Misc.Pause(1200)
        
    else:
        Player.HeadMessage(77,"You are out of eggs") 
        Misc.Pause(1200)
        Misc.ScriptStop("Jaf's_smokebomb_craft.py")
    
def getginseng():
    sGinseng = Items.FindByID(0x0F85,0x0000,supplyChest)
    Misc.Pause(200)
    count = Items.ContainerCount(supplyChest,0x0F85,0x0000)
    if count > 3:
        Items.Move(sGinseng,Player.Backpack.Serial,150)
        Misc.Pause(1200)
    else:
        Player.HeadMessage(77,"You are out of Ginseng") 
        Misc.Pause(1200)
        Misc.ScriptStop("Jaf's_smokebomb_craft.py")
        
def makesmoke():
    Items.UseItemByID(0x0E9B,-1)
    Gumps.WaitForGump(460, 10000)
    Gumps.SendAction(460, 83)
    Misc.Pause(200)
    
    
def makeLast():
    Gumps.WaitForGump(460, 5000)
    Gumps.SendAction(460, 1999)
    if Journal.Search('You have worn out your tool!') == True:
        Journal.Clear()
        checkTools()
        Misc.Pause(300)
        Items.UseItemByID(0x0E9B,-1)
        Misc.Pause(500)
    Journal.Clear()
    Misc.Pause(200)
    
def moveSmokeb():
    Smokeb = Items.FindByID(0x2808,0x0000,Player.Backpack.Serial)
    Items.Move(Smokeb,supplyChest,0)
    Misc.Pause(1200)
    
def smokeLoop():
    makesmoke()
    while Items.BackpackCount(0x2808,0x0000) < 50:
        checkSupplies()
        makeLast()
    moveSmokeb()    
    
def main():
    Items.UseItem(supplyChest)
    Misc.Pause(1200)
    checkSupplies()
    checkTools()
    smokeLoop()

    
while True:
    main()    