# JustanotherFace (JaF) for RE; JaF's Potion and Apple Chug with Trap Box Smoke Bombs and Invis Pots
# Original V1.0: 01/14/2023 
# Current Version V1.2: 01/24/2023
# 
# Setup:
# Set healHits to your hit point number you want to drink a greater heal potion at
# Set stampts to the stamina point number you want to drink a greater refreshment potion at
# Set hideHits to the hit point number you want to hide at
# Set pophits to the hit points not to use a trap box below
# Set usetrap true or false to use or not use trapbox
# Set useinv true or false to use or not use invis pots if smoke timer is active
# Set useapp true or false to use or not use enchanted apples
# Set usebomb true or false to use or not use smokebombs 

import sys
from System.Collections.Generic import List

usetrap = True
useinv = True
useapp = True
usebomb = True
#######################################################################################################################
healHits = 75 # Edit this number to change hit points at which to use Greater Heal pots
stampts = 100 # Edit this number to change stam points at which to use Greater Refresh pots
hideHits = 40 # Edit this number to change hit points to hide at using smoke bomb or invis pot
pophits = 50 ## Edit this number to change hit points not to use trap below. This will keep you from trap boxing to death

#######################################################################################################################
healPot = 0x0F0C # greater heal pot itemid
curePot = 0x0F07 # greater cure pot itemid
stamPot = 0x0F0B # greater refresh pot itemid
apple = 0x2FD8 # enchanted apple itemid
bomb = 0x2808 #smokebomb itemid
invpots = 0x0F06 #invisibility pot itemid
trap = 0x09A9 # this is the itemid of a small crate trap box. If you use anything but a small crate trapbox change this
#######################################################################################################################



while True:

    if Player.Hits <= healHits and Player.Visible and not Player.Poisoned and not Player.BuffsExist('Mortal Strike') and Timer.Check("healpottimer") == False:            
        Items.UseItemByID(healPot)               
        Misc.Pause(400)
        Timer.Create("healpottimer", 10500)
        
    elif Player.BuffsExist('Paralyze') and Player.Visible and usetrap == True and Player.Hits >= pophits:
        Items.UseItemByID(trap)
        Misc.Pause(400)
        
    elif Player.Hits <= hideHits and Player.Visible and usebomb == True and not Player.Poisoned and not Player.BuffsExist('Mortal Strike') and Timer.Check("hidehittimer") == False:            
        Items.UseItemByID(bomb)               
        Misc.Pause(400)
        Timer.Create("hidehittimer", 10500)
        
    elif Player.Hits <= hideHits and Player.Visible and useinv == True and not Player.Poisoned and not Player.BuffsExist('Mortal Strike') and Timer.Check("hidehittimer") == True:            
        Items.UseItemByID(invpots)         
        Misc.Pause(400)
    
    elif Player.Stam <= stampts and Player.Visible and not Player.Poisoned and not Player.BuffsExist('Mortal Strike') and Timer.Check("stampottimer") == False:
        Items.UseItemByID(stamPot)
        Misc.Pause(400)
        Timer.Create("stampottimer", 10500)
    

    elif Player.Poisoned and not Player.BuffsExist('Mortal Strike') and not Player.BuffsExist('Orange Petals') and Player.Visible:
        Items.UseItemByID(curePot)
        Misc.Pause(400)

    elif useapp == True and Player.BuffsExist('Mortal Strike') or Player.BuffsExist('Sleep') or Player.BuffsExist('Blood Oath(curse)') or Player.BuffsExist('Curse') or Player.BuffsExist('Bleed') or Player.BuffsExist('Corpse Skin') and Timer.Check("appletimer") == False:
        Misc.Pause(2500)
        Items.UseItemByID(apple)
        Misc.Pause(400)
        Timer.Create("appletimer", 30500)
    else:
        Misc.Pause(400)
        

  