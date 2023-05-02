import time, random, climage
from colored import fg, bg, attr

print(f'{fg(5)}Elden Ring Beta testing{attr(0)}')
time.sleep(3)
print(f'{fg(5)}   Elden Ring Beta {attr(0)}')
time.sleep(3)

logo = climage.convert('Start.png', width=110, is_unicode=True, is_truecolor=True, palette="default", is_8color=False, is_16color=False, is_256color=False)
print(logo)
time.sleep(4)
start2 = str(input(""))
menu2 = climage.convert('menu.png', width=110, is_unicode=True, is_truecolor=True, palette="default", is_8color=False, is_16color=False, is_256color=False)
print(menu2)
time.sleep(2)
print('Press N for new game, S for settigs, Q for quitting')
menu = str(input(''))
if menu == "N" or menu == 'n':
        print("Questo e un gioco rpg, dove incontrerai Npc di ogni genere, Boss unici,\nCombattimenti fino all'ultimo sangue e dialoghi tra te e gli Npc")
        time.sleep(4)
        print('Prima di tutto inserire il proprio nome....')
        time.sleep(2)
        nome=str(input(''))
        print(f'Sei sicoro che {nome} sia quello giusto?')
        time.sleep(2)
        risposta = str(input(''))

        if risposta == 'Si' or risposta == 'si':
            print('Bene')
            time.sleep(2)
        else:         
            print('Inserire il nome desiderato..')    
            nome=str(input('')) 

        #scelta del personaggio
        print('ora devi scegliere la tua classe....')
        time.sleep(2)
        print('Cavaliere errante            Profeta                    Samurai\nStatistiche                  Statistiche                Statistiche \nLivello totale: 9            Livello totale: 7          Livello totale: 9 \nVitalità: 15                 Vitalità: 10               Vitalità: 12 \nMente: 10                    Mente: 14                  Mente: 11 \nTempra: 11                   Tempra: 8                  Tempra: 13 \nForza: 14                    Forza: 11                  Forza: 12 \nDestrezza: 13                Destrezza: 10              Destrezza: 15 \nIntelligenza: 9              Intelligenza: 7            Intelligenza: 9\nFede: 9                      Fede: 16                   Fede: 8 \nArcano: 7                    Arcano: 10                 Arcano: 8')


        scelta = int(input('Che classe vuoi scegliere(1=cavaliere 2=profeta 3=Samurai): '))  

        if scelta != 0 or scelta < 4:
            print(f'Bene....')
            print('che la tua avventura inizi....')
if menu == "S" or menu == 's':
        print("|-------------------|")
        print("|****** Lingua******|")
        print("|-------------------|")

        lingua = str(input('Selezionare lingua(L): '))
        if lingua == 'L' or lingua == 'l':
            print('|-------------------|')
            print('|******Inglese******|')
            print('|******Italiano*****|')
            print('|******Tedesco******|')
            print('|-------------------|')
            change = str(input('Selezionare la lingua(E ing, I ita, T ted): '))

            if change == "E" or change == 'e':

                print("Good")

                menu3 = climage.convert('menu.png', width=110, is_unicode=True, is_truecolor=True, palette="default", is_8color=False, is_16color=False, is_256color=False)
                print(menu3)                                                                                           
                time.sleep(2)                
                print('Press N for new game, S for settigs, Q for quitting')
                menu = str(input(''))
                if menu == "N" or menu == 'n':
                    print('Welcome to Elden Ring, this is a rpg game with Npc and Boss battle.')
                    time.sleep(4)
                    print('First in first you need to select a name: ')
                    time.sleep(2)
                    nome=str(input(''))
                    print(f'Are you sure that {nome} is the correct one? ')
                    time.sleep(2)
                    risposta = str(input(''))

                    if risposta == 'Yes' or risposta == 'yes':
                        print('Good')
                        time.sleep(2)
                    else:         
                        print('Try a new name.. : ')    
                        nome=str(input('')) 

                    #scelta del personaggio
                    print('Review of the classes..')
                    class_1 = climage.convert('Knight.png', width=60, is_unicode=True, is_truecolor=True, palette="default", is_8color=False, is_16color=False, is_256color=False)
                    print(f'{fg(5)}{class_1} 1{attr(0)}')
                    time.sleep(5)
                    class_2 = climage.convert('Mage.png', width=60, is_unicode=True, is_truecolor=True, palette="default", is_8color=False, is_16color=False, is_256color=False)
                    print(f'{fg(5)}{class_2} 2{attr(0)}')
                    time.sleep(5)
                    class_3 = climage.convert('Samurai.png.png', width=60, is_unicode=True, is_truecolor=True, palette="default", is_8color=False, is_16color=False, is_256color=False)
                    print(f'{fg(5)}{class_3} 3{attr(0)}')
                    time.sleep(5)
                    print('Now select a class to review it..')
                    review = int(input(''))
                    if review == 1:
                        print('Cavaliere errante\nStatistiche\nLivello totale: 9\nVitalità: 15\nMente: 10\nTempra: 11\nForza: 14\nDestrezza: 13\nIntelligenza: 9\nFede: 9\nArcano: 7')
                    if review == 2:    
                        print('Profeta\nStatistiche\nLivello totale: 7\nVitalità: 10\nMente: 14\nTempra: 8\nForza: 11\nDestrezza: 10\nIntelligenza: 7\nFede: 16\nArcano: 10')
                    if review == 3:    
                        print('Samurai\nStatistiche\nLivello totale: 9 \nVitalità: 12 \nMente: 11 \nTempra: 13 \nForza: 12 \nDestrezza: 15 \nIntelligenza: 9\nFede: 8 \nArcano: 8')
                    
                    print('Good now you must select the class that you wanna play..')                 

                    scelta = int(input(''))  

                    if scelta != 0 or scelta < 4:

                        print('Good')
                        print('That the adventure begin')
                        
                        def loadingE():
                            print('.....loading 0.......')
                            time.sleep(2)
                            print('.....loading 5.......')
                            time.sleep(2)
                            print('.....loading 10.......')
                            time.sleep(2)
                            print('.....loading 15.......')
                            time.sleep(2)
                            print('.....loading 20.......')
                            time.sleep(2)
                            print('.....loading 25.......')
                            time.sleep(2)
                            print('.....loading 30.......')
                            time.sleep(2)
                            print('.....loading 40.......')
                            time.sleep(2)
                            print('.....loading 50.......')
                            time.sleep(2)
                            print('.....loading 60.......')
                            time.sleep(2)
                            print('.....loading 70.......')
                            time.sleep(2)
                            print('.....loading 80.......')
                            time.sleep(2)
                            print('.....loading 90.......')
                            time.sleep(2)
                            print('.....loading finish.......')
                            time.sleep(2)

                        def startgameE():
                            print('A Tarnished of no renown. Cross the fog, to the Lands Between, to stand before the Elden Ring.')
                            time.sleep(5)
                            print(f'Welcome tarnished')
                            time.sleep(2)
                            print('You awake is a place of you unknown, wanna go outside?')
                            move = str(input(''))
                            if move == 'Yes' or move == 'yes':
                                print('....')
                                time.sleep(2)
                                print('....')
                                time.sleep(2)
                                print('....')
                                time.sleep(2)
                                print('<You hear a noise>')
                                time.sleep(2)
                                print('<Fall noises>')
                                time.sleep(2)        
                                print('A Boss appears in front of you.')
                                time.sleep(2)
                                print('     Grafted Scion       ')
                                time.sleep(2)
                                print('Statistic: \nhealth: 2596 \ndifence:107')
                                time.sleep(2)
                                print('Your damage is 65 and your Hp is 800')
                                time.sleep(2)
                                print('For now you can only attack...')
                                time.sleep(2)
                                att = str(input('Press a to attack: ')) 
                                if att == 'A' or att == 'a':
                                    player_life = 800
                                    boss_life = 2596

                                    while player_life > 0 and boss_life > 0: #un loop infinito, che finira con la tua morte
                                        print("Your hp:", player_life)
                                        print("Boss hp:", boss_life)
                                        boss_hit = random.randint(0, 250)
                                        Pdamage = 65
                                        boss_life -= Pdamage
                                        player_life -= boss_hit
                                        print("You deal " + str(Pdamage) + " damage to the Boss!")
                                        print("You take " + str(boss_hit) + " damage!")

                                    if boss_life <= 0:
                                            print('Its impossible >:<') #Nel gioco, il primo boss ti deve uccidere o ti uccidi per andare avanti...
                                    else:
                                        print("The boss win!")
                                        time.sleep(2)
                                        print('.....')
                                        time.sleep(1)
                                        print('.....')
                                        time.sleep(1)
                                        print('.....')
                                        time.sleep(1)
                                        print('.....')
                                        time.sleep(1)
                                        print('.....')
                                        time.sleep(1)
                                        print('unknown = Wake up... Its not your time to die...')
                                        time.sleep(3)
                                        print('..<sigh>..')
                                        time.sleep(2)
                                        print('You wake up...')
                                        time.sleep(2)
                                        print('You are in the catacombs... Wanna explore them?')
                                        move1 = str(input(''))
                                        if move1 == 'Yes' or move1 == 'yes':
                                            print('You explore the catacombs and you find a elevator')
                                            time.sleep(2)
                                            print('When you arrive on the top, you see a door')
                                            time.sleep(2)
                                            print('Wanna open it?')                        
                                            open = str(input(''))
                                            if open == 'Yes' or open == 'yes':
                                                print('...<opening rumors>...')
                                                time.sleep(2)
                                                print('...<door is opening>...')
                                                time.sleep(2)
                                                print('<Limgrave>')
                                                time.sleep(2)
                                                print('You see a person sit on a rock')
                                                time.sleep(2)
                                                print('And you decide to approach him..')
                                                time.sleep(2)
                                                #Introduzione al primo Npc che ti blastera =_=
                                                print(f'{fg(6)}Stranger = ah....Tarnished...are we?{attr(0)}')
                                                time.sleep(4)
                                                print(f'{fg(6)}Stranger = ...Come to the land of between for the elden ring, hmmm?{attr(0)}')
                                                time.sleep(4)
                                                print(f'{fg(6)}Stranger = Of course you have. No shame in it...{attr(0)}')
                                                time.sleep(3)
                                                print(f'{fg(6)}Stranger = But unfortunately for you.. You are maidenless..{attr(0)}')
                                                time.sleep(3)
                                                print(f'{fg(6)}Stranger = Without guidance, without the strength of runes, and without an invitation to the Roundtable Hold..{attr(0)}')
                                                time.sleep(5)
                                                print(f'{fg(6)}Stranger = You are fated, it seen, to die in obscurity...{attr(0)}')
                                                time.sleep(4)
                                                print('After he rekt you. You decide to go...')

                        def NpcsE():
                            global runedrop, rune
                            time.sleep(2)
                            print('You start going to the castle that you saw early')
                            time.sleep(2)
                            print('suddently a Npc comes from far')
                            time.sleep(2)
                            print('Wanna figth him?')
                            fight = str(input(''))
                            if fight == 'Yes' or fight == 'yes':
                                player_life = 1000
                                Npc_life = 420

                                while player_life > 0 and Npc_life > 0: #stesso loop come il primo boss
                                    print("Your hp:", player_life)
                                    print("Npc's hp:", Npc_life)
                                    Npc_hit1 = random.randint(0, 200)
                                    player_hit = 65
                                    Npc_life -= player_hit
                                    player_life -= Npc_hit1
                                    print("You deal to the Npc's ", player_hit, "hp")
                                    print("Npc's deal ", Npc_hit1, "hp")
                                    

                                    if Npc_life <= 0:
                                        print("Npc fell")
                                        time.sleep(2)
                                        runedrop = random.randint(0,200)
                                        print(f'You got {runedrop} runes')
                                        rune = 0
                                        rune = rune + runedrop
                                        print(f'You now have {rune} runes')
                                        
                                        print('You go over but you see 2 Npc')
                                        time.sleep(2)
                                        print('Dp you wanna fight them?')
                                        fight2 = str(input(''))
                                        if fight2 == 'Yes' or fight2 == 'yes':
                                            player_life = 1000
                                            Npc_life1 = 840
                                            while player_life > 0 and Npc_life1 > 0: #stesso loop come il primo boss
                                                print("Your hp:", player_life)
                                                print("Npc's hp:", Npc_life1)
                                                Npc_hit1 = random.randint(0, 200)
                                                player_hit = 65
                                                Npc_life1 -= player_hit
                                                player_life -= Npc_hit1
                                                print("You deal to the Npc's ", player_hit, "hp")
                                                print("Npc's deal ", Npc_hit1, "hp")
                                                if Npc_life1 <= 0:
                                                    print("Npc's got defeated")
                                                    runedrop = random.randint(0,400)
                                                    print(f'You got {runedrop} runes')
                                                    rune = 0
                                                    rune = rune + runedrop
                                                    print(f'You now have {rune} runes')
                                                    
                                                    
                                                else:
                                                    print('You got defeated, next time will be better....') 
                                    else:
                                        print('You got defeated, next time will be better....') 
                                        
                        

                        
                        def BossFightE():
                            global Pdamage, difence, player_life
                            time.sleep(2)
                            print("You arrive to the entrance of the castle")
                            time.sleep(2)
                            print('Do you enter?')
                            enter = str(input(''))
                            if enter == "Yes" or enter == "yes":                                
                                time.sleep(2)
                                print('You go over the entrace...Later on you see a bridge..')
                                time.sleep(2)
                                print('Do you take it?')
                                move2 = str(input(''))
                                if move2 == "Yes" or move2 == "yes":
                                    print('You walk in')
                                    time.sleep(2)
                                    print('.......')
                                    time.sleep(2)
                                    print('.......')
                                    time.sleep(2)
                                    print('.......')
                                    time.sleep(2)
                                    #Primo dialogo del Boss
                                    print('<Unknown voice>')                                    
                                    time.sleep(2)
                                    print(f'{fg(52)}Unknown = Foul Tarnished{attr(0)}')
                                    time.sleep(3)
                                    print(f'{fg(52)}Unknown = in search of the elden ring{attr(0)}')
                                    time.sleep(3)
                                    print(f'{fg(52)}Unknown = Emboldened by the flame of ambition{attr(0)}')
                                    time.sleep(5)
                                    print('<Jump>')
                                    time.sleep(2)
                                    print('<Fall noise>')
                                    time.sleep(2)
                                    print('.......')
                                    time.sleep(2)
                                    print('.......')
                                    time.sleep(2)
                                    print(f'{fg(52)}Unknown = Someone must extinguish thy flame{attr(0)}')
                                    time.sleep(3)
                                    print(f'{fg(52)}Unknown = Let it be Margit the Fell!{attr(0)}')
                                    time.sleep(2)
                                                                        
                                    print(f'{fg(52)}<Margit the fell Omen>{attr(0)}')
                                                                                
                                    Pdamage = 85
                                    player_life =  1500
                                    difence = 65
                                    margit = 4174
                                                                                
                                    # inizii vedendo la tua vita e qulla del boss                                                                                                    
                                    while player_life > 0 and margit > 0:
                                        print("Your hp is: " + str(player_life))
                                        print("The Boss hp is: " + str(margit))
                                        choice = input("Wanna attack or parry? a/p : ")
                                        if choice == "a":
                                            if margit <= 2087:
                                                break
                                            margit = margit - Pdamage
                                            print("You deal " + str(Pdamage) + " damage to the Boss!")
                                            crit = random.randint(0,6)                                                            
                                            if crit == 6:
                                                blood_lost = 1400
                                                player_crit=(Pdamage + 65 + blood_lost)
                                                margit = margit - player_crit
                                                print("You deal " + str(player_crit) + " damage to the Boss!")
                                            bossA = random.randint(0,1)
                                            if bossA == 1:
                                                Bdamage = random.randint(50,200)
                                                player_life = player_life - Bdamage
                                                print("You take " + str(Bdamage) + " damage!")
                                                                                            
                                        elif choice == "p":
                                            if margit <= 2087:
                                                break
                                            Bdamage = random.randint(50,200)                                                                
                                            player_life = player_life - (Bdamage - difence)
                                            print("You take " + str(Bdamage) + " damage!")
                                            playerA = random.randint(0,1)
                                            if playerA == 1:                                                                
                                                margit = margit - Pdamage
                                                print("You deal " + str(Pdamage) + " damage to the Boss!") 
                                                                                                
                                        else:
                                            print("Unknown command!")                                                                                             
                                                                                            
                                    
                                                                                    
                                    #seconda fase        
                                    print(f'{fg(52)}Margit = Well, thou art of passing skill.{attr(0)}')
                                    time.sleep(2)
                                    print(f'{fg(52)}Margit = Warrior blood must truly run in thy veins, Tarnished.{attr(0)}')
                                    time.sleep(2)
                                    #il danno aumenta durante la seconda fase
                                    while player_life > 0 and margit > 0:
                                        print("Your hp is: " + str(player_life))
                                        print("The Boss hp is: " + str(margit))
                                        choice = input("Wanna attack or parry? a/p : ")
                                        if choice == "a":
                                            margit = margit - Pdamage
                                            print("You deal " + str(Pdamage) + " damage to the Boss!")
                                            crit = random.randint(0,6)                                                            
                                            if crit == 6:
                                                blood_lost = 1400
                                                player_crit=(Pdamage + 65 + blood_lost)
                                                margit = margit - player_crit
                                                print("You deal " + str(player_crit) + " damage to the Boss!")
                                            bossA = random.randint(0,1)
                                            if bossA == 1:
                                                Bdamage = random.randint(100,250)
                                                player_life = player_life - Bdamage
                                                print("You take " + str(Bdamage) + " damage!")
                                                                                            
                                        elif choice == "p":
                                            Bdamage = random.randint(100,250)                                                                
                                            player_life = player_life - (Bdamage - difence)
                                            print("Hai subito " + str(Bdamage) + " danni!")
                                            playerA = random.randint(0,1)
                                            if playerA == 1:                                                                
                                                margit = margit - Pdamage
                                                print("You deal " + str(Pdamage) + " damage to the Boss!") 
                                                                                                
                                        else:
                                            print("Unknown command!")
                                                                                            
                                    #indico cosa succede se si muore o se si vince
                                                                                    
                                    if player_life <= 0:
                                        print("You lose, next time be more strong")
                                        time.sleep(2)
                                        
                                    if margit <= 0:
                                        print("You won!")
                                        time.sleep(2)
                                        print('<Geat Enemy Fellen>')
                                        time.sleep(2)
                                        print(f"{fg(52)}Margit: I shall remember thee, Tarnished.{attr(0)}")
                                        time.sleep(4)
                                        print(f"{fg(52)}Margit: Smould'ring with thy meagre flame.{attr(0)}")
                                        time.sleep(4)
                                        print(f"{fg(52)}Margit: Cower in fear. Of the night.{attr(0)}")
                                        time.sleep(3)
                                        print(f"{fg(52)}Margit: The hands of the Fell Omen shall brook thee no quarter.{attr(0)}")
                                        time.sleep(6)
                                        BossdropM = 12000
                                        print(f'You got {BossdropM} runes')                                        
                                        rune = rune + BossdropM
                                        print(f'You now have {rune} runes')                                                
                                        print('You pass the bridge..')
                                        time.sleep(2)
                                        print('After you pass the bridge you see the capital')
                                        time.sleep(2)
                                        print('You decide to go..')
                                        time.sleep(2)
                                        print('.....')
                                        time.sleep(2)
                        def Npcs2E():
                            global Pdamage, difence, player_life
                            print("A Npc spawn in front of you and decide to approuch you...")
                            time.sleep(2)
                                                                
                            Npc_life = 640
                            
                            while player_life > 0 and Npc_life > 0:
                                print("Your hp:", player_life)
                                print("Npc's hp:", Npc_life)
                                Npc_hit1 = random.randint(0, 200)
                                player_hit = 85
                                Npc_life -= player_hit
                                player_life -= Npc_hit1
                                print("You deal to the Npc's ", player_hit, "hp")
                                print("Npc's deal ", Npc_hit1, "hp")
                                if Npc_life <= 0:
                                    print("Npc fell..")
                                    time.sleep(2)
                                    print('You start going to the capital...')
                                else:
                                    print('You got defeated, next time will be better....')
                                    runedrop = random.randint(0,400)
                                    print(f'You got {runedrop} runes')
                                    rune = 0
                                    rune = rune + runedrop
                                    print(f'You now have {rune} runes')

                        def CapitalE():
                            time.sleep(2)
                            print('....')
                            time.sleep(2)
                            print('<noise>')
                            time.sleep(2)
                            print('You look behind you')
                            time.sleep(2)
                            print(f'{fg(6)}Unknown: Hello {nome}.. Did you lose yourself?{attr(0)}')
                            talk = str(input(''))
                            if talk == 'No' or talk=='no':
                                print(f'{fg(6)}Unknown: Ohh really; You look like you lose yourself, hehe{attr(0)}')
                                time.sleep(2)
                                print(f'{fg(6)}Unknown: Where are you going?{attr(0)}')
                                time.sleep(2)
                                print('<Press 1 to say that you are going to the capital\nPress 2 to say that its not your business>')
                                quesito = str(input(''))  
                                if quesito == 1:
                                    print(f'{fg(6)}Unknown: Oh, you go to the capital.. stay safe tarnished.. that place is very dangerous.{attr(0)}')
                                    time.sleep(2)  
                                    print(f'{fg(6)}Unknown: Stay safe....{attr(0)}')
                                    time.sleep(2)
                                    print('<he go away>')
                                    time.sleep(2)
                                    print('You go fowards...')
                                    time.sleep(2)
                                    print("Another Npc spawn in front of you and decide to approuch you..")
                                    Npc_life = 640
                                    player_life = 1500                                                            
                                    while player_life > 0 and Npc_life > 0:                                                                                                 
                                                                        
                                        print("Your hp:", player_life)
                                        print("Npc's hp:", Npc_life)
                                        Npc_hit1 = random.randint(0, 200)
                                        player_hit = 85
                                        Npc_life -= player_hit
                                        player_life -= Npc_hit1
                                        print("You deal to the Npc's ", player_hit, "hp")
                                        print("Npc's deal ", Npc_hit1, "hp")
                                        if Npc_life <= 0:
                                            print("Npc fell..")
                                            time.sleep(2)
                                            runedrop = random.randint(0,400)
                                            print(f'You got {runedrop} runes')
                                            rune = 0
                                            rune = rune + runedrop
                                            print(f'You now have {rune} runes')
                                            print('You keep going to the capital')
                                            time.sleep(2)
                                            print('Keep going')
                                            time.sleep(2)
                                            print("You keep going and you arrive to the capital")
                                            time.sleep(2)    
                                            print('You go fowards...')
                                            time.sleep(2)
                                            ('.....')
                                            time.sleep(2)
                                            print('You try to find a way to go to the Elden Ring')
                                            time.sleep(2)
                                            print('You walk for a whyle and...')        

                                if quesito == 2:
                                    print(f'{fg(6)}Unknown: Oh, I get it.. You dont trust me... its ok. I will do it too{attr(0)}')
                                    time.sleep(2)                                    
                                    print('<he go away>')
                                    time.sleep(2)
                                    print('You go fowards...')
                                    print('.....')
                                    time.sleep(2)
                                    print("Another Npc spawn in front of you and decide to approuch you..")
                                    Npc_life = 640
                                    player_life = 1500                                                            
                                    while player_life > 0 and Npc_life > 0:                                                                                                 
                                                                        
                                        print("Your hp:", player_life)
                                        print("Npc's hp:", Npc_life)
                                        Npc_hit1 = random.randint(0, 200)
                                        player_hit = 85
                                        Npc_life -= player_hit
                                        player_life -= Npc_hit1
                                        print("You deal to the Npc's ", player_hit, "hp")
                                        print("Npc's deal ", Npc_hit1, "hp")
                                        if Npc_life <= 0:
                                            print("Npc fell..")
                                            time.sleep(2)
                                            runedrop = random.randint(0,400)
                                            print(f'You got {runedrop} runes')
                                            rune = 0
                                            rune = rune + runedrop
                                            print(f'You now have {rune} runes')
                                            print('You keep going to the capital')
                                            time.sleep(2)
                                            print('Keep going')
                                            time.sleep(2)
                                            print("You keep going and you arrive to the capital")
                                            time.sleep(2)    
                                            print('You go fowards...')
                                            time.sleep(2)
                                            ('.....')
                                            time.sleep(2)
                                            print('You try to find a way to go to the Elden Ring')
                                            time.sleep(2)
                                            print('You walk for a whyle and...')             
                            if talk == 'Yes' or talk=='yes':
                                print(f'{fg(6)}Unknown: I knew that... let me help you...{attr(0)}')
                                time.sleep(3)
                                print('<teletrasport>')
                                time.sleep(2)
                                print('You got teletrasported to the capital..')
                                time.sleep(2)
                                print('You try to find a way to go to the Elden Ring')
                                time.sleep(2)
                                print('You walk for a whyle and...')  
                            
                            

                        
                        def Npcs4E():                                        
                            print("A capital knight approuch you.")
                            Cknight = 1040
                            player_life = 1500                                                            
                            while player_life > 0 and Cknight > 0:                                                                                                 
                                                                
                                print("Your hp:", player_life)
                                print("Npc's hp:", Cknight)
                                Npc_hit1 = random.randint(50, 350)
                                player_hit = 85
                                Cknight -= player_hit
                                player_life -= Npc_hit1
                                print("You deal to the Npc's ", player_hit, "hp")
                                print("Npc's deal ", Npc_hit1, "hp")
                                if Cknight <= 0:
                                    print("Npc fell..")
                                    runedrop = random.randint(0,600)
                                    print(f'You got {runedrop} runes')
                                    rune = 0
                                    rune = rune + runedrop
                                    print(f'You now have {rune} runes')
                                    time.sleep(2)
                                    print('You keep going..')
                                    time.sleep(2)
                                    print('.....')
                                    time.sleep(2)
                                    print('After you walk for some time you finally arrive to the Elden Ring')
                                    time.sleep(2)
                                    print('You enter in the big room')
                                    time.sleep(2)
                                    print('......')
                                else:
                                    print('You got defeate, be sure to be more strong next time')
                        def Boss_fight2E():
                            
                            print('<Boss room>')
                            time.sleep(2)
                            print('.....')
                            time.sleep(3)
                            print(f'{fg(52)}Unknown: Graceless Tarnished.{attr(0)}')                                                                                                        
                            time.sleep(5)
                            print(f'{fg(52)}Unknown: What is thy business with these thrones.{attr(0)}')
                            time.sleep(4)
                            print(f'{fg(52)}Unknown: ahh...{attr(0)}')
                            time.sleep(4)                                                                                                   
                            print(f'{fg(52)}Unknown: Godrick the Golden.{attr(0)}')
                            time.sleep(4)
                            print(f'{fg(52)}Unknown: The twin prodigies, Miquella and Malenia.{attr(0)}')
                            time.sleep(4)
                            print(f'{fg(52)}Unknown: General Radahn.{attr(0)}')
                            time.sleep(2)
                            print(f'{fg(52)}Unknown: Praetor Rykard.{attr(0)}')
                            time.sleep(2)
                            print(f'{fg(52)}Unknown: Lunar Pricess Ranni.{attr(0)}')
                            time.sleep(5)
                            print(f'{fg(52)}Unknown: Wilful traitors,all.{attr(0)}')
                            time.sleep(4)
                            print(f'{fg(52)}Unknown: Thy kind all of a piece.{attr(0)}')
                            time.sleep(4)
                            print(f'{fg(52)}Unknown: Pillagers. Emboldened by the flame of ambition.{attr(0)}')
                            time.sleep(5)
                            print(f'{fg(52)}Unknown: Have it writ upon thy meagre grave.{attr(0)}')
                            time.sleep(3)
                            print(f'{fg(52)}Morgot: Fell by King Morgot! Last of all kings.{attr(0)}')
                            time.sleep(2)
                                                                                                        
                            print('<Morgot the Omen king>')
                            
                            morgot = 10399
                                                                            
                            # inizii vedendo la tua vita e qulla del boss                                                                                                    
                            while player_life > 0 and morgot > 0:
                                print("Your hp is: " + str(player_life))
                                print("The Boss hp is: " + str(morgot))
                                choice = input("Wanna attack or parry? a/p : ")
                                if choice == "a":
                                    if morgot <= 5199:
                                        break
                                    morgot = morgot - Pdamage
                                    print("You deal " + str(Pdamage) + " damage to the Boss!")
                                    crit = random.randint(0,6)                                                            
                                    if crit == 6:
                                            blood_lost = 1600
                                            player_crit=(Pdamage + 105 + blood_lost)
                                            morgot = morgot - player_crit
                                            print("You deal " + str(player_crit) + " damage to the Boss!")
                                    bossA = random.randint(0,3)
                                    if bossA == 3:
                                            Bdamage = random.randint(200,300)
                                            player_life = player_life - Bdamage
                                            print("You take " + str(Bdamage) + " damage!")
                                                                                            
                                elif choice == "p":
                                    if morgot <= 5199:
                                        break
                                    Bdamage = random.randint(200,300)                                                                
                                    player_life = player_life - (Bdamage - difence)
                                    print("You take " + str(Bdamage) + " damage!")
                                    playerA = random.randint(0,1)
                                    if playerA == 1:                                                                
                                        morgot = morgot - Pdamage
                                        print("You deal " + str(Pdamage) + " damage to the Boss!") 
                                                                                                
                                else:
                                        print("Unknown command!")                                                                                             
                                                                                        
                                
                                                                                    
                            #seconda fase        
                            print(f'{fg(52)}Morgot = Hrhaaaahar{attr(0)}')
                            time.sleep(4)
                            print(f'{fg(52)}Morgot = These thrones..... stained by my curse....{attr(0)}')
                            time.sleep(3)
                            print(f'{fg(52)}Morgot = Such a shame I cannot bear.{attr(0)}')
                            time.sleep(3)
                            print(f'{fg(52)}Morgot = Thy part in this shall not be forgiven{attr(0)}')
                            time.sleep(3)
                            #il danno aumenta durante la seconda fase
                            while player_life > 0 and morgot > 0:
                                print("Your hp is: " + str(player_life))
                                print("The Boss hp is: " + str(morgot))
                                choice = input("Wanna attack or parry? a/p : ")
                                if choice == "a":
                                    if morgot <= 5199:
                                        break
                                    morgot = morgot - Pdamage
                                    print("You deal " + str(Pdamage) + " damage to the Boss!")
                                    crit = random.randint(0,6)                                                            
                                    if crit == 6:
                                            blood_lost = 1600
                                            player_crit=(Pdamage + 105 + blood_lost)
                                            morgot = morgot - player_crit
                                            print("You deal " + str(player_crit) + " damage to the Boss!")
                                    bossA = random.randint(0,3)
                                    if bossA == 3:
                                            Bdamage = random.randint(250,450)
                                            player_life = player_life - Bdamage
                                            print("You take " + str(Bdamage) + " damage!")
                                                                                            
                                elif choice == "p":
                                    if morgot <= 5199:
                                        break
                                    Bdamage = random.randint(250,450)                                                                
                                    player_life = player_life - (Bdamage - difence)
                                    print("You take " + str(Bdamage) + " damage!")
                                    playerA = random.randint(0,1)
                                    if playerA == 1:                                                                
                                        morgot = morgot - Pdamage
                                        print("You deal " + str(Pdamage) + " damage to the Boss!") 
                                                                                                
                                else:
                                        print("Unknown command!")                           
                                                                                            
                            #indico cosa succede se si muore o se si vince
                                                                                
                            if player_life <= 0:
                                print("Hai perso!")
                                time.sleep(2)
                                
                                    
                            if morgot <= 0:
                                print("Hai vinto!")
                                time.sleep(2)
                                print('<Geat Enemy Fellen>')
                                time.sleep(2)
                                print(f"{fg(52)}Morgot: ...{attr(0)}")
                                time.sleep(4)
                                print(f"{fg(52)}Morgot: Tarnished, thou'rt but a fool.{attr(0)}")
                                time.sleep(4)
                                print(f"{fg(52)}Morgot: The Erdtree wards off all who deign approach{attr(0)}")
                                time.sleep(4)
                                print(f"{fg(52)}Morgot: We are...we are all forsaken{attr(0)}")
                                time.sleep(4)                                
                                print('<Strong wind>')
                                time.sleep(2)
                                print('sconosciuto: Sorry..')
                                time.sleep(2)
                                print('<Colpo>')
                                time.sleep(2)
                                print('You get it by behind and you fall...')
                                time.sleep(2)

                        
                        
                        loadingE()
                        startgameE()
                        NpcsE()
                        
                        BossFightE()
                        Npcs2E()
                        CapitalE()                        
                        Npcs4E()
                        Boss_fight2E()
                if menu == "I" or menu == 'i':
                    print(f'{fg(3)}                                                                          |----------------------| {attr(0)}')
                    print(f'{fg(3)}                                                                          |******Elden Ring******| {attr(0)}')
                    print(f'{fg(3)}                                                                          |******          ******| {attr(0)}')
                    print(f'{fg(3)}                                                                          |****** New Game ******| {attr(0)}')
                    print(f'{fg(3)}                                                                          |****** Settings ******| {attr(0)}')
                    print(f'{fg(3)}                                                                          |******   Quit   ******| {attr(0)}')
                    print(f'{fg(3)}                                                                          |----------------------| {attr(0)}')
                    time.sleep(2)                    
                    print('Press N for new game, S for settigs, Q for quitting')
                    menu = str(input(''))
                    if menu == "N" or menu == 'n':
                        print("Questo e un gioco rpg, dove incontrerai Npc di ogni genere, Boss unici,\nCombattimenti fino all'ultimo sangue e dialoghi tra te e gli Npc")
                        time.sleep(4)
                        print('Prima di tutto inserire il proprio nome....')
                        time.sleep(2)
                        nome=str(input(''))
                        print(f'Sei sicoro che {nome} sia quello giusto?')
                        time.sleep(2)
                        risposta = str(input(''))

                        if risposta == 'Si' or risposta == 'si':
                            print('Bene')
                            time.sleep(2)
                        else:         
                            print('Inserire il nome desiderato..')    
                            nome=str(input('')) 

                        #scelta del personaggio
                        print('Ora guarda le classi')
                        class_1 = climage.convert('Knight.png', is_unicode=True,)
                        print(f'{fg(5)}{class_1} 1{attr(0)}')
                        time.sleep(5)
                        class_2 = climage.convert('Mage.png', is_unicode=True,)
                        print(f'{fg(5)}{class_2} 2{attr(0)}')
                        time.sleep(5)
                        class_3 = climage.convert('Samurai.png.png', is_unicode=True,)
                        print(f'{fg(5)}{class_3} 3{attr(0)}')
                        time.sleep(5)
                        print('Now select a class to review it..')
                        review = int(input(''))
                        if review == 1:
                            print('Cavaliere errante\nStatistiche\nLivello totale: 9\nVitalità: 15\nMente: 10\nTempra: 11\nForza: 14\nDestrezza: 13\nIntelligenza: 9\nFede: 9\nArcano: 7')
                        if review == 2:    
                            print('Profeta\nStatistiche\nLivello totale: 7\nVitalità: 10\nMente: 14\nTempra: 8\nForza: 11\nDestrezza: 10\nIntelligenza: 7\nFede: 16\nArcano: 10')
                        if review == 3:    
                            print('Samurai\nStatistiche\nLivello totale: 9 \nVitalità: 12 \nMente: 11 \nTempra: 13 \nForza: 12 \nDestrezza: 15 \nIntelligenza: 9\nFede: 8 \nArcano: 8')
                        
                        print('Bane ora devi scegliere quale giocare..') 

                        scelta = int(input(''))  

                        if scelta != 0 or scelta < 4:
                            print(f'Bene....')
                            print('che la tua avventura inizi....')
                            

                            def loading():
                                print('.....loading 0.......')
                                time.sleep(2)
                                print('.....loading 5.......')
                                time.sleep(2)
                                print('.....loading 10.......')
                                time.sleep(2)
                                print('.....loading 15.......')
                                time.sleep(2)
                                print('.....loading 20.......')
                                time.sleep(2)
                                print('.....loading 25.......')
                                time.sleep(2)
                                print('.....loading 30.......')
                                time.sleep(2)
                                print('.....loading 40.......')
                                time.sleep(2)
                                print('.....loading 50.......')
                                time.sleep(2)
                                print('.....loading 60.......')
                                time.sleep(2)
                                print('.....loading 70.......')
                                time.sleep(2)
                                print('.....loading 80.......')
                                time.sleep(2)
                                print('.....loading 90.......')
                                time.sleep(2)
                                print('.....loading finish.......')
                                time.sleep(2)

                            def startgame():
                                print('A Tarnished of no renown. Cross the fog, to the Lands Between, to stand before the Elden Ring.')
                                time.sleep(5)
                                print(f'Welcome tarnished')
                                time.sleep(2)
                                print('Sei in un palazzo sconoscuto a te e non ti ricordi niente vuoi proseguire?')
                                move = str(input(''))
                                if move == 'Si' or move == 'si':
                                    print('....')
                                    time.sleep(2)
                                    print('....')
                                    time.sleep(2)
                                    print('....')
                                    time.sleep(2)
                                    print('<Senti un rumore>')
                                    time.sleep(2)
                                    print('<rumore di una caduta>')
                                    time.sleep(2)        
                                    print('Un boss appare davanti a te')
                                    time.sleep(2)
                                    print('     Grafted Scion       ')
                                    time.sleep(2)
                                    print('statistiche: \nvita: 2596 \ndifesa:107')
                                    time.sleep(2)
                                    print('il tuo danno e di 65hp al secondo, e la tua vita e di 800hp')
                                    time.sleep(2)
                                    print('Per adesso puoi solo attacare....')
                                    time.sleep(2)
                                    att = str(input('Inserire ,a, per attacare: ')) 
                                    if att == 'A' or att == 'a':
                                        player_life = 800
                                        boss_life = 2596

                                        while player_life > 0 and boss_life > 0: #un loop infinito, che finira con la tua morte
                                            print("Vita del giocatore:", player_life)
                                            print("Vita del boss:", boss_life)
                                            boss_hit = random.randint(0, 250)
                                            Pdamage = 65
                                            boss_life -= Pdamage
                                            player_life -= boss_hit
                                            print("Il giocatore colpisce il boss per", Pdamage, "vita")
                                            print("Il boss colpisce il giocatore per", boss_hit, "vita")

                                        if boss_life <= 0:
                                                print('non e possibile, adesso........') #Nel gioco, il primo boss ti deve uccidere o ti uccidi per andare avanti...
                                        else:
                                            print("Il boss ha vinto!")
                                            time.sleep(2)
                                            print('.....')
                                            time.sleep(1)
                                            print('.....')
                                            time.sleep(1)
                                            print('.....')
                                            time.sleep(1)
                                            print('.....')
                                            time.sleep(1)
                                            print('.....')
                                            time.sleep(1)
                                            print('sconosciuto = Non e ancora arrivata la tua ora, svegliati')
                                            time.sleep(3)
                                            print('..<sigh>..')
                                            time.sleep(2)
                                            print('ti alzi...')
                                            time.sleep(2)
                                            print('ti ritrovi dentro delle catacombe... vuoi proseguire?')
                                            move1 = str(input(''))
                                            if move1 == 'Si' or move1 == 'si':
                                                print('ti incammini e trovi un ascensore..')
                                                time.sleep(2)
                                                print('salito, trovi un portone vuoi aprirlo?')
                                                    
                                                open = str(input(''))
                                                if open == 'Si' or open == 'si':
                                                    print('...<rumori di apertura>...')
                                                    time.sleep(2)
                                                    print('...<porta aperta>...')
                                                    time.sleep(2)
                                                    print('<Limgrave>')
                                                    time.sleep(2)
                                                    print('Vedi una persona in piedi vicino a un masso e ti avvicini')
                                                    time.sleep(2)
                                                    #Introduzione al primo Npc che ti blastera =_=
                                                    print('Stranger = ah....Tarnished...are we?')
                                                    time.sleep(4)
                                                    print('Stranger = ...Come to the land of between for the elden ring,hmmm?')
                                                    time.sleep(3)
                                                    print('Stranger = Of course you have. No shame in it...')
                                                    time.sleep(3)
                                                    print('Stranger = But unfortunately for you.. You are maidenless..')
                                                    time.sleep(3)
                                                    print('Stranger = Without guidance, without the strength of runes, and without an invitation to the Roundtable Hold..')
                                                    time.sleep(4)
                                                    print('Stranger = You are fated, it seen, to die in obscurity...')
                                                    time.sleep(3)
                                                    print('te ne vai....')

                            def Npcs():
                                time.sleep(2)
                                print('inizii a incamminarti verso il castello in lontananza..')
                                time.sleep(2)
                                print('improvisamnete compare un nemico')
                                time.sleep(2)
                                print('Cosa fai lo affronti?')
                                fight = str(input(''))
                                if fight == 'Si' or fight == 'si':
                                    player_life = 800
                                    Npc_life = 420

                                    while player_life > 0 and Npc_life > 0: #stesso loop come il primo boss
                                        print("Vita del giocatore:", player_life)
                                        print("Vita dell' Npc:", Npc_life)
                                        Npc_hit = random.randint(0, 50)
                                        player_hit = 65
                                        Npc_life -= player_hit
                                        player_life -= Npc_hit
                                        print("Il giocatore colpisce l'Npc per", player_hit, "vita")
                                        print("L'Npc colpisce il giocatore per", Npc_hit, "vita")

                                    if Npc_life <= 0:
                                        print("L'Npc e caduto")
                                        time.sleep(2)
                                        print('Prosegui e trovi altri due Npc')
                                        time.sleep(2)
                                        print('li vuoi combattere?')
                                        fight2 = str(input(''))
                                        if fight2 == 'Si' or fight2 == 'si':
                                            player_life = player_life + 800
                                            Npc_life1 = 840
                                            while player_life > 0 and Npc_life1 > 0: #stesso loop come il primo boss
                                                print("Vita del giocatore:", player_life)
                                                print("Vita dell'Npc", Npc_life1)
                                                Npc_hit1 = random.randint(0, 200)
                                                player_hit = 65
                                                Npc_life1 -= player_hit
                                                player_life -= Npc_hit1
                                                print("Il giocatore colpisce gli Npc  per", player_hit, "vita")
                                                print("Gli Npc colpiscono il giocatore per", Npc_hit1, "vita")
                                                if Npc_life1 <= 0:
                                                    print("Gli Npc sono caduti")
                                                else:
                                                    print('Sei stato sconfitto...ritenta') 
                                    else:
                                        print('Sei stato sconfitto...ritenta') 
                            def BossFight():
                                print('Ti incammini per il castello..')
                                time.sleep(2)
                                print('.....')
                                time.sleep(2)
                                print("Prosegui e ti ritrovi davanti alla porta del castello...")
                                time.sleep(2)
                                print('Entri?')
                                enter = str(input(''))
                                if enter == "Si" or enter == "si":
                                    print('Entri...')
                                    time.sleep(2)
                                    print('Prosegui per un po e vedi un ponte..')
                                    time.sleep(2)
                                    print('lo prendi?')
                                    move2 = str(input(''))
                                    if move2 == "Si" or move2 == "si":
                                        print('Cammini')
                                        time.sleep(2)
                                        print('.......')
                                        time.sleep(2)
                                        print('.......')
                                        time.sleep(2)
                                        print('.......')
                                        time.sleep(2)
                                        #Primo dialogo del Boss
                                        print('<Voce sconosciuta>')
                                        time.sleep(2)
                                        print('sconosciuto = Foul Tarnished')
                                        time.sleep(3)
                                        print('sconosciuto = in search of the elden ring')
                                        time.sleep(3)
                                        print('sconosciuto = Emboldened by the flame of ambition')
                                        time.sleep(4)
                                        print('<Salto>')
                                        time.sleep(2)
                                        print('<Rumore di una caduta>')
                                        time.sleep(2)
                                        print('.......')
                                        time.sleep(2)
                                        print('.......')
                                        time.sleep(2)
                                        print('sconosciuto = Someone must extinguish thy flame\nLet it be Margit the Fell!')
                                        time.sleep(3)
                                        print('sconosciuto = Let it be Margit the Fell!')
                                        time.sleep(2)
                                                                                    
                                                                                    
                                        print('<Margit the fell Omen>')
                                                                                    
                                        player_life = player_life + 800
                                        Pdamage = 85                                            
                                        difesa = 50
                                        margit = 4174
                                                                                    
                                        # inizii vedendo la tua vita e qulla del boss
                                                                                                                                
                                        while player_life > 0 and margit > 0:
                                            print("Il tuo hp è: " + str(player_life))
                                            print("L'hp del boss è: " + str(margit))
                                            choice = str(input("Vuoi attaccare o parare? a/p: "))
                                            #due opzioni 
                                                                                        
                                            if choice == "a":
                                                margit = margit - Pdamage
                                                print("Hai inflitto " + str(Pdamage) + " danni al boss!")
                                                crit = random.randint(0,6) #se ti capita 6 infliggerai un danno critico + danno da effetto                                                            
                                                if crit == 6:
                                                    blood_lost = 1400
                                                    player_crit=(Pdamage + 65 + blood_lost)
                                                    margit = margit - player_crit
                                                    print("Hai inflitto " + str(player_crit) + " danni al boss!")
                                                bossA = random.randint(0,3) # mentre il boss a una possibilita su 4 di colpirti
                                                if bossA == 3:
                                                    Bdamage = random.randint(0,100)
                                                    player_life = player_life - Bdamage
                                                    print("Hai subito " + str(Bdamage) + " danni!")
                                                if margit <= 2087: #quando il boss arriva a meta vita finisce il while e inizia la sua seconda fase
                                                    break
                                                                                                
                                            elif choice == "p":
                                                Bdamage = random.randint(0,100)
                                                if margit <= 2087:
                                                    break
                                                player_life = player_life - (Bdamage - difesa)
                                                print("Hai subito " + str(Bdamage) + " danni!")
                                                playerA = random.randint(0,1)
                                                if playerA == 1:                                                                
                                                    margit = margit - Pdamage
                                                    print("Hai inflitto " + str(Pdamage) + " danni al boss!") 
                                                                                                    
                                                                                                
                                            else:
                                                print("Scelta non valida!")
                                                                                        
                                        #seconda fase        
                                        print('Margit = Well, thou art of passing skill.')
                                        time.sleep(2)
                                        print('Margit = Warrior blood must truly run in thy veins, Tarnished.')
                                        time.sleep(2)
                                        #il danno aumenta durante la seconda fase
                                        while player_life > 0 and margit > 0:
                                            print("Il tuo hp è: " + str(player_life))
                                            print("L'hp del boss è: " + str(margit))
                                            choice = input("Vuoi attaccare o parare? a/p")
                                            if choice == "a":
                                                margit = margit - Pdamage
                                                print("Hai inflitto " + str(Pdamage) + " danni al boss!")
                                                crit = random.randint(0,6)                                                            
                                                if crit == 6:
                                                    blood_lost = 1400
                                                    player_crit=(Pdamage + 65 + blood_lost)
                                                    margit = margit - player_crit
                                                    print("Hai inflitto " + str(player_crit) + " danni al boss!")
                                                    bossA = random.randint(0,1)
                                                if bossA == 1:
                                                    Bdamage = random.randint(100,250)
                                                    player_life = player_life - Bdamage
                                                    print("Hai subito " + str(Bdamage) + " danni!")
                                                                                                
                                            if choice == "p":
                                                Bdamage = random.randint(100,250)                                                                
                                                player_life = player_life - (Bdamage - difesa)
                                                print("Hai subito " + str(Bdamage) + " danni!")
                                                playerA = random.randint(0,1)
                                                if playerA == 1:                                                                
                                                    margit = margit - Pdamage
                                                    print("Hai inflitto " + str(Pdamage) + " danni al boss!") 
                                                                                                    
                                            else:
                                                print("Scelta non valida!")
                                                                                                
                                        #indico cosa succede se si muore o se si vince
                                                                                        
                                        if player_life <= 0:
                                            print("Hai perso!")
                                            time.sleep(2)
                                            
                                        if margit <= 0:
                                            print("Hai vinto!")
                                            time.sleep(2)
                                            print('<Geat Enemy Fellen>')
                                            time.sleep(2)                                            
                                            print("Margit: I shall remember thee, Tarnished.")
                                            time.sleep(2)
                                            print("Margit: Smould'ring with thy meagre flame.")
                                            time.sleep(2)
                                            print("Margit: Cower in fear. Of the night.")
                                            time.sleep(2)
                                            print("Margit: The hands of the Fell Omen shall brook thee no quarter.")
                                            time.sleep(6)                                                
                                            print('You pass the bridge..')
                                            time.sleep(2)
                                            print('Superato il ponte vedi in lontananza una città')
                                            time.sleep(2)
                                            print('ti incammini....')
                                            time.sleep(2)
                                            print('.....')
                                            time.sleep(2)
                        def Npcs2():
                            print("comprare un'Npc e ti sfida")
                            time.sleep(2)
                                                                
                            Npc_life = 640
                            player_life = 1500
                                            
                            while player_life > 0 and Npc_life > 0:
                                print("Your hp:", player_life)
                                print("Npc's hp:", Npc_life)
                                Npc_hit1 = random.randint(0, 200)
                                player_hit = 85
                                Npc_life -= player_hit
                                player_life -= Npc_hit1
                                print("You deal to the Npc's ", player_hit, "hp")
                                print("Npc's deal ", Npc_hit1, "hp")
                                if Npc_life <= 0:
                                    print("Npc fell..")
                                    time.sleep(2)
                                    print('You start going to the capital...')
                                else:
                                    print('You got defeated, next time will be better....')

                        def Capital():
                            time.sleep(2)
                            print('....')
                            time.sleep(2)
                            print('<rumors>')
                            time.sleep(2)
                            print('You look behind you')
                            time.sleep(2)
                            print(f'Unknown: Hello {nome}.. Did you lose yourself?')
                            talk = str(input(''))
                            if talk == 'No' or talk=='no':
                                print('Unknown: Ohh really; You look like you lose yourself, hehe')
                                time.sleep(2)
                                print('Unknown: Where are you going?')
                                time.sleep(2)
                                print('<Press 1 to say that you are going to the capital\nPress 2 to say that its not your business>')
                                quesito = str(input(''))  
                                if quesito == 1:
                                    print('Unknown: Oh, you go to the capital.. stay safe tarnished.. that place is very dangerous.')
                                    time.sleep(2)  
                                    print('Unknown: Stay safe....')
                                    time.sleep(2)
                                    print('<he go away>')
                                    time.sleep(2)
                                    print('You go fowards...')
                                    time.sleep(2)

                                if quesito == 2:
                                    print('sconosciuto: Capisco non ti fidi degli sconoscuti, lo farei anche io')
                                    time.sleep(2)
                                    print('<se ne va>')
                                    time.sleep(2)
                                    print('Tu prosegui per il sentiero')
                                    time.sleep(2)
                                    print('.....')
                                    time.sleep(2)
                                    
                            else:
                                print('Unknown: I knew that... let me help you...')
                        def Npcs3():                                        
                            print("Un'altro Npc compare e ti sfida")                                                            
                            while player_life > 0 and Npc_life > 0:
                                Npc_life = 640
                                player_life = 1500                                                                  
                                                                
                                print("Your hp:", player_life)
                                print("Npc's hp:", Npc_life)
                                Npc_hit1 = random.randint(0, 200)
                                player_hit = 85
                                Npc_life -= player_hit
                                player_life -= Npc_hit1
                                print("You deal to the Npc's ", player_hit, "hp")
                                print("Npc's deal ", Npc_hit1, "hp")
                                if Npc_life <= 0:
                                    print("Npc fell..")
                                    time.sleep(2)
                                    print('Prosegui per poi arrivare davanti alla porta della capitale...')
                                    time.sleep(2)
                                    print('Prosegui..')
                                    time.sleep(2)
                                    print("Percorri dei sentieri e ti imbatti in un ponte che porte ai piedi dell'ErdTree")#ErdTree e l'albero gigante del gioco, chiamato anche Elden Ring
                                    time.sleep(2)    
                                    print('You go fowards...')
                                    time.sleep(2)
                                    ('.....')
                                    time.sleep(2)
                        def Boss_fight2():
                            print('<Boss room>')
                            time.sleep(2)
                            print('.....')
                            time.sleep(3)
                            print('Unknown: Graceless Tarnished.')                                                                                                        
                            time.sleep(5)
                            print('Unknown: What is thy business with these thrones.')
                            time.sleep(4)
                            print('Unknown: ahh...')
                            time.sleep(4)                                                                                                   
                            print('Unknown: Godrick the Golden.')
                            time.sleep(4)
                            print('Unknown: The twin prodigies, Miquella and Malenia.')
                            time.sleep(4)
                            print('Unknown: General Radahn.')
                            time.sleep(2)
                            print('Unknown: Praetor Rykard.')
                            time.sleep(2)
                            print('Unknown: Lunar Pricess Ranni')
                            time.sleep(5)
                            print('Unknown: Wilful traitors,all.')
                            time.sleep(4)
                            print('Unknown: Thy kind all of a piece.')
                            time.sleep(4)
                            print('Unknown: Pillagers. Emboldened by the flame of ambition.')
                            time.sleep(5)
                            print('Unknown: Have it writ upon thy meagre grave.')
                            time.sleep(3)
                            print('Morgot: Fell by King Morgot! Last of all kings.')
                            time.sleep(2)
                                                                                                        
                            print('<Morgot the Omen king>')
                                                                                            
                                            


                            loading()
                            startgame()
                            Npcs()
                            BossFight()
                            Npcs2()
                            Capital()
                            Npcs3()
                            Boss_fight2()