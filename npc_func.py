import time
import random

def fight_npc():
    player_life = 1000
    Npc_life = 420
    Pdamage=50
    blood_lost=1800
    defence=25
    while player_life > 0 and Npc_life > 0: #stesso loop come il primo Npc_life
        choice = input("Do you want to attack or parry? (a/p): \n")
        if choice == "a":
            Npc_life = Npc_life - Pdamage
            print(f"You dealt {Pdamage} damage to the Npc_life!")
            crit = random.randint(0,6)
            if crit == 6:
                player_crit=(Pdamage + 65 + blood_lost)
                Npc_life = Npc_life - player_crit
                print(f"You dealt {player_crit} damage to the Npc_life!")
            Npc_lifeA = random.randint(0,1)
            if Npc_lifeA == 1:
                Ndamage = random.randint(50,200)
                player_life = player_life - Ndamage
                print(f"You took {Ndamage} damage!")

        elif choice == "p":
            Ndamage = random.randint(50,200)
            player_life = player_life - (Ndamage - defence)
            print(f"You took {Ndamage} damage!")
            playerA = random.randint(0,1)
            if playerA == 1:
                Npc_life = Npc_life - Pdamage
                print(f"You dealt {Pdamage} damage to the Npc_life!")
        else:
            print("Unknown command!")
    if Npc_life <= 0:
        print("Npc died")
        time.sleep(2)
    if player_life<= 0:
        print("You died")
        time.sleep(2)