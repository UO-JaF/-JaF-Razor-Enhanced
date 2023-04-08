# JustanotherFace (JaF) RE; JaF's Thorn Planter
# Current V1.1: 04/08/2023
# Added thorn count and halt script if no thorns. You must save
# the script as the correct script name for Halt to work "JaF's thorn planter V1.1.py"
# Original V1.0: 04/02/2023 
#
def plant():
    if Items.BackpackCount(0x0F42,0x0042) < 1:
        Misc.ScriptStop("JaF's thorn planter V1.1.py")
    while Timer.Check("thorntime"):
        remain = (Timer.Remaining("thorntime"))
        total_seconds = int(remain / 1000)
        minutes       = int(total_seconds / 60)
        seconds       = int(total_seconds - minutes * 60)
        Misc.SendMessage("Time Left: {} Minutes {:02} Seconds".format(minutes,seconds))
        Misc.Pause(5000)
    if Timer.Check('thorntime') == False:
        Player.ChatSay(52, "All Follow Me")
        Misc.Pause(500)
        Player.ChatSay(52, "All Guard Me")
        Items.UseItemByID(0x0F42,0x0042)#green thorns
        Target.WaitForTarget(10000, False)
        Target.TargetExecuteRelative(Player.Serial,0)
        Timer.Create("thorntime",180000)
        # attack()
        
while not Player.IsGhost:
    plant()
    
