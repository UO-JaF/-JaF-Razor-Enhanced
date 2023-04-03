#JustAnotherFace Trapbox Healing - First RE script Initial release V1.0 08-30-2022
#Current version V1.1 release 09-26-2022
#Set your healing and anatomy max skill level you want to achieve below


healingmax = 85 #Change this to the max healing skill you want
anatomymax = 85 #Change this to the max anatomy skill you want
#Don't change anything below this line
#-------------------------------------------------------------------
trap = Items.FindByID(0x09A9, -1, Player.Backpack.Serial)#This finds a crate in your backpack

def Trapbox():

    Items.UseItem ( trap )
    Misc.Pause(2200)
    healBelowMax()
    if Player.Hits == Player.HitsMax:
        TrainHealing()

def healBelowMax(): 
    bandages = Items.FindByID( 0x0E21, -1, Player.Backpack.Serial )    
    while Player.Hits < Player.HitsMax and bandages != None:
        Items.UseItem( bandages )
        Target.WaitForTarget( 2000, False )
        Target.TargetExecute( Player.Serial )
        Misc.Pause(6200)

    if Player.Hits == Player.HitsMax and bandages != None:
        TrainHealing()
    else:
        Player.HeadMessage( 178, 'You need bandages!' )
        Misc.ScriptStop("JAF-Trapbox-Heal.py")
        
def TrainHealing():
    if Player.GetRealSkillValue('Anatomy') >= anatomymax:
            Player.SetSkillStatus('Anatomy', 2)
    if Player.GetRealSkillValue('Healing') >= healingmax:
            Player.SetSkillStatus('Healing', 2)
    if Player.GetRealSkillValue( 'Healing' ) >= healingmax and Player.GetRealSkillValue('Anatomy') >= anatomymax:
        Player.SetSkillStatus('Healing', 2)
        Player.SetSkillStatus('Anatomy', 2)
        Player.HeadMessage( 178, 'You are at your Healing and Anatomy Skill Cap! Skills are locked ' )        
        Misc.ScriptStop("JAF-Trapbox-Heal.py")
    if Player.GetRealSkillValue('Anatomy') >= anatomymax and Player.GetRealSkillValue('Healing') < healingmax:
        Player.SetSkillStatus('Anatomy', 2)
        Misc.Pause(500)
        Trapbox()
    if Player.GetRealSkillValue('Healing') >= healingmax and Player.GetRealSkillValue ('Anatomy') < anatomymax:
        Player.SetSkillStatus('Healing', 2)
        Misc.Pause(500)
        Trapbox()


Trapbox()
healBelowMax()
TrainHealing()