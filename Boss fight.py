import random
from colored import fg, bg, attr
import time
import numpy as np
def stat():
    vet = np.zeros([])
    filename = 's.py'
    with open(filename) as file:
        for line in file:
            df = int(line.rstrip())
            for i in range(1):
                vet = np.append(vet, df)
        return vet
def first_phase():
    global el,Pdamage,player_life,defence,blood_lost,Boss,halfHP,pl
    vet=stat()
    el=np.delete(vet, 0)
    Pdamage = el[0] + 20
    player_life =  el[1] + 400
    defence = el[2] + 15
    blood_lost = el[3] + 200
    Boss = 4070
    halfHP = Boss  / 2
    pl = player_life
    while pl > 0 and Boss>0:
        print(f"Your health points are: {player_life}")
        print(f"The Boss health points are: {Boss}" ) 
        choice = input("Do you want to attack or parry? (a/p): \n")
        if choice == "a":
            if Boss <= halfHP:
                break
            Boss = Boss - Pdamage
            print(f"You dealt {Pdamage} damage to the Boss!")
            crit = random.randint(0,6)
            if crit == 6:
                player_crit=(Pdamage + 65 + blood_lost)
                Boss = Boss - player_crit
                print(f"You dealt {player_crit} damage to the Boss!")
            bossA = random.randint(0,1)
            if bossA == 1:
                Bdamage = random.randint(50,200)
                player_life = player_life - Bdamage
                print(f"You took {Bdamage} damage!")

        elif choice == "p":
            if Boss <= halfHP:
                break
            Bdamage = random.randint(50,200)
            player_life = player_life - (Bdamage - defence)
            print(f"You took {Bdamage} damage!")
            playerA = random.randint(0,1)
            if playerA == 1:
                Boss = Boss - Pdamage
                print(f"You dealt {Pdamage} damage to the Boss!")
        else:
            print("Unknown command!")
    #seconda fase        
def sec_phase(player_life):
    global Boss, Pdamage, defence
    #il danno aumenta durante la seconda fase
    while player_life > 0 and Boss > 0:
        print(f"Your health points are: {player_life}")
        print(f"The Boss health points are: {Boss}" )
        choice = input("Do you want to attack or parry? (a/p): \n")
        if choice == "a":
            Boss = Boss - Pdamage
            print(f"You dealt {Pdamage} damage to the Boss!")
            crit = random.randint(0,6)                                                            
            if crit == 6:
                blood_lost = 1400
                player_crit=(Pdamage + 65 + blood_lost)
                Boss = Boss - player_crit
                print(f"You dealt {player_crit} damage to the Boss!")
            bossA = random.randint(0,1)
            if bossA == 1:
                Bdamage = random.randint(100,250)
                player_life = player_life - Bdamage
                print(f"You took {Bdamage} damage!")
                                                            
        elif choice == "p":
            Bdamage = random.randint(100,250)                                                                
            player_life = player_life - (Bdamage - defence)
            print(f"You took {Bdamage} damage!")
            playerA = random.randint(0,1)
            if playerA == 1:                                                                
                Boss = Boss - Pdamage
                print(f"You dealt {Pdamage} damage to the Boss!") 
                                                                
        else:
            print("Unknown command!")
                                                            
    #indico cosa succede se si muore o se si vince
                                                    
    if player_life <= 0:
        print("You lost next time come back stronger")   
        
        
    if Boss <= 0:
        print("You won!")



first_phase()
#dialogo
sec_phase(player_life)
