# JustanotherFace (JaF) 2nd script for RE; JaF's Move Champ Scrolls to Books
# Original V1.0: 09/08/2022 Current V1.7 09/21/2022
#
# Shoutout to Dalamar, Credzba and Juggz for the help!
# And for being patient with a newbie. Thanks guys!
# This script is to move PowerScrolls, Transcendence Scrolls, 
# and Primer On "x" Mastery scrolls from your player backpack to 
# a Powerscroll book, a transcendence book and since there is 
# currently no Primer book, primers are moved into a container
# of your choice. 
#
# The scroll books must be locked down in your house.
# You can use 2 Scroll books, it will ask you to Target
# Your 105 book and your 110 - 120 book. If you only have
# one book for all scrolls, target that book for 105 and 110+
#
# You must have a trashcan to trash in reach Level 1 Primers 
# Get near the books and the container for Primers
# Press play and follow the instruction messages on lower left
# side of your screen.  


from System.Collections.Generic import List 
scrolls = [
0x14EF,
0x1E22
]

trashcan = Target.PromptTarget("Select your Trash Can")
Misc.Pause(1200)    
wondcontainer = Target.PromptTarget("Select your container to move Shitty 105 Scrolls to")
Misc.Pause(1200)
wcontainer = Target.PromptTarget("Select your container to move White 110, 115 and 120 Scrolls to")
Misc.Pause(1200)
pcontainer = Target.PromptTarget("Select your container to move Pink Scrolls to")
Misc.Pause(1200)
twopricontainer = Target.PromptTarget("Select your container to move Level 2 Primer Scrolls to")
Misc.Pause(1200)
threepricontainer = Target.PromptTarget("Select your container to move Level 3 Primer Scrolls to")
Misc.Pause(1200)

mycontainer = Target.PromptTarget("Select your container you want to move scrolls FROM")
Misc.Pause(1200)

def movethem():

    backpack = Items.FindBySerial(mycontainer)
    for scroll in backpack.Contains:
        if scroll.ItemID in scrolls:
            if scroll.Hue == 0x0481 : # Whites
                Items.WaitForProps(scroll, 1100)
                Misc.Pause(500)
                props = (Items.GetPropStringList(scroll))
                Misc.Pause(500)
                prop = props[0].split(' ')[1]
                Misc.Pause(500)
                if "wondrous" in 'props' .join(Items.GetPropStringList(scroll)):
                    Player.HeadMessage(178, "Moving Your Shitty 105's")
                    Items.Move(scroll,wondcontainer, 0)
                    Misc.Pause(600)
                else:
                    Items.Move(scroll,wcontainer, 0)
                    Player.HeadMessage(178, "Moving 110, 115 and 120's")
                    Misc.Pause(600)
                
            elif scroll.Hue == 0x0490 : #Pinks
                Player.HeadMessage(178, "Moving Transcendance scroll")
                Items.Move(scroll,pcontainer, 0)
                Misc.Pause(1200)
            
            else: # Primers
                Items.WaitForProps(scroll, 1100)
                Misc.Pause(500)
                props = (Items.GetPropStringList(scroll))
                Misc.Pause(500)
                prop = props[0].split(' ')[1]
                Misc.Pause(500)
                if "Volume III" in 'props' .join(Items.GetPropStringList(scroll)):
                    Player.HeadMessage(178, "Moving Your Level 3 Primer")
                    Items.Move(scroll,threepricontainer, 0)
                    Misc.Pause(1200)
                elif "Volume II" in 'props' .join(Items.GetPropStringList(scroll)):
                    Player.HeadMessage(178, "Moving Your Level 2 Primer")
                    Items.Move(scroll,twopricontainer, 0)
                    Misc.Pause(1200)
                elif "Volume I" in 'props' .join(Items.GetPropStringList(scroll)):
                    Player.HeadMessage(178, "Trashing Your Shitty Level 1 Primer")
                    Items.Move(scroll,trashcan, 0)
                    Misc.Pause(600)

movethem()            
Player.HeadMessage (178, "Get to Fel and get some scrolls Loser! Your scroll pack is empty")
Misc.Pause(1200)
