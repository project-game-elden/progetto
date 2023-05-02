
import random
import numpy as np
vet = np.zeros([])
filename = 's.py'
with open(filename) as file:    
    for line in file:    
        df = int(line.rstrip())
        for i in range(1):
            vet = np.append(vet, df)         
el=np.delete(vet, 0)
Pdamage = el[0] + 20
player_life =  el[1] + 400
difence = el[2] + 15
blood_lost = el[3] + 200
Boss = 4070
halfHP = Boss  / 2
pl = player_life
while pl > 0 and Boss>0:
    print("Your hp is: " + str(player_life))
    print("The Boss hp is: " + str(Boss)) 
    choice = input("Wanna attack or parry? a/p : ")     
    if choice == "a":
        if Boss <= halfHP:
            break
        Boss = Boss - Pdamage
        print("You deal " + str(Pdamage) + " damage to the Boss!")
        crit = random.randint(0,6)                                                            
        if crit == 6:                
            player_crit=(Pdamage + 65 + blood_lost)
            Boss = Boss - player_crit
            print("You deal " + str(player_crit) + " damage to the Boss!")
        bossA = random.randint(0,1)
        if bossA == 1:
            Bdamage = random.randint(50,200)
            player_life = player_life - Bdamage
            print("You take " + str(Bdamage) + " damage!")
                                                        
    elif choice == "p":
        if Boss <= halfHP:
            break
        Bdamage = random.randint(50,200)                                                                
        player_life = player_life - (Bdamage - difence)
        print("You take " + str(Bdamage) + " damage!")
        playerA = random.randint(0,1)
        if playerA == 1:                                                                
            Boss = Boss - Pdamage
            print("You deal " + str(Pdamage) + " damage to the Boss!")                                                                 
    else:
        print("Unknown command!")