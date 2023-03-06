# JustanotherFace (JaF): JaF's Tamer All Kill
# Original V1.0: 03/04/2023 Current V1.0 03/04/2023
#
# This script will honor (if in range for honor), tell your pet to follow(all follow) and tell your pet to kill(all kill)
# any monster or player who is grey or red and NOT on your friends list. 
import time
import sys
import math
from System.Collections.Generic import List
from System import Byte, Int32
#
ignore = []
def attack():
    while not Player.IsGhost:
        enemy = None
        enemy_filter = Mobiles.Filter()
        enemy_filter.Enabled = True
        enemy_filter.RangeMin = -1
        enemy_filter.RangeMax = 8
        enemy_filter.IsGhost = False
        enemy_filter.Friend = False
        enemy_filter.CheckLineOfSight = True
        enemy_filter.Notorieties = List[Byte](bytes([3,4,5,6]))
        enemy_filter.ZLevelMin = Player.Position.Z - 8
        enemy_filter.ZLevelMax = Player.Position.Z + 8
        
        enemies = Mobiles.ApplyFilter(enemy_filter)
        
        remove_mine = []
        for e in enemies:
            owner = Mobiles.GetPropValue(e.Serial, "Owner")
            if owner == Player.Name:
                remove_mine.append(e)
        if len(remove_mine) != 0:        
            for e in remove_mine:
                enemies.Remove(e)
                Misc.SendMessage("Removed one")
        
        if len(enemies) > 0 :
            enemy = Mobiles.Select(enemies, 'Nearest')
            curTarget = enemy
                
        while enemy != None and not Player.IsGhost: 
            Player.InvokeVirtue('Honor')
            Target.WaitForTarget(1500)
            Target.TargetExecute(enemy)
            Misc.Pause(500)
            Player.ChatSay(44, "All Follow")
            Target.WaitForTarget(1500)
            Target.TargetExecute(enemy)
            Player.ChatSay(52, "All kill")
            Target.WaitForTarget(2000, True)
            Target.TargetExecute(enemy)
            Mobiles.Message(enemy, 5, "Attacking 0x{:08x}".format(enemy.Serial))
            Mobiles.Message(enemy, 5, "Attacking {:08x} ".format(enemy.MobileID))
            Timer.Create("longkill", 60000)
            while Mobiles.FindBySerial(enemy.Serial): 
                while Timer.Check("longkill") == False:
                    Mobiles.Message(enemy, 5, "Original Target Still {:08x} ".format(enemy.Serial))
                    Player.ChatSay(44, "All Follow")
                    Target.WaitForTarget(1500)
                    Target.TargetExecute(enemy)
                    Player.ChatSay(52, "All kill")
                    Target.WaitForTarget(2000, True)
                    Target.TargetExecute(enemy)
                    Timer.Create("longkill", 60000)
                    
            
            while not Mobiles.FindBySerial(enemy.Serial):
                Player.ChatSay(52, "All Follow Me")
                Misc.Pause(500)
                Player.ChatSay(52, "All Guard Me")
                attack()

attack()