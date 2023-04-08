# JustanotherFace (JaF) RE; JaF's Egg Sorter
# Original V1.0: 04/02/2023 Current V1.1 04/06/2022
# Updated to auto open the containers when you select them
# You need a container to put your Rare eggs into
# Press Play and follow directions on bottom left of screen

import System
from System.Collections.Generic import List
from System import Byte
from System import Int32
eggs = [
0x9F13,
0x9F14,
0x9F15,
0x9F16,
0x9F17,
0x9F18,
0x9F19
]

colors = [
0x044b,
0x044c,
0x048D,
0x048E,
0x0789,
0x089A,
0x09C6,
0x0AA1,
0x081B,
0x081C,
0x0AB0,
0x0AC1,
0x0AC6,
0x0AC7
]

ignore = []

rarecan = Target.PromptTarget("Select a container to put your rare colored eggs in TO.")
Misc.Pause(1200)
Items.UseItem(rarecan)
Misc.Pause (1200)    

mycontainer = Target.PromptTarget("Select your container you want to move rare eggs FROM")
Misc.Pause(1200)
Items.UseItem(mycontainer)
Misc.Pause (1200)    

def movethem():

    backpack = Items.FindBySerial(mycontainer)
    for egg in backpack.Contains:
        if egg.ItemID in eggs:
            if egg.Hue in colors : # Whites
                Player.HeadMessage (178, "Moving Rare Egg")
                Items.Move(egg,rarecan, 0)
                Misc.Pause(1400)
            else:
                if egg.Hue not in colors and egg.Serial not in ignore:
                    ignore.append(egg.Serial)
movethem() 