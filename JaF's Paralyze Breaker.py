# JustanotherFace (JaF) for RE; JaF's Paralyze Breaker
# Original V1.0: 01/11/2023 
# Set pophits to your hit point number you want to be above before using trap box
# Set stampts to the stamina point number you want to drink a greater refreshment potion at
#
# 

import sys
from System.Collections.Generic import List

pophits = 50 ## Edit this number to change hit points not to use trap below
trap = 0x09A9

 
while True:
    if Player.BuffsExist('Paralyze') and Player.Hits >= pophits:
        Misc.Pause(600)
        Items.UseItemByID(trap)
        Misc.Pause(400)
        
    else:
        Misc.Pause(400)