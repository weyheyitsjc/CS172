#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172

from jacyschamps import Bunny
from jacyschamps import Pikachu
from justinslosers import HandsomeSquidward
from justinslosers import Thanos
import random

#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

    #first reset everyone's health!
    m1.resetHealth()
    m2.resetHealth()

    #next print out who is battling
    print("Starting Battle Between")
    print(m1.getName()+": "+m1.getDescription())
    print(m2.getName()+": "+m2.getDescription())
    
    
    #Whose turn is it?
    attacker = None
    defender = None
    
    x = random.randint(1,100)
    
    if x <= 25:
        attacker = m1
        defender = m2
    elif (x > 25 and x <= 50):
        attacker = m2
        defender = m1
    elif (x > 50 and x <= 75):
        attacker = m1
        defender = m2
    else:
        attacker = m2
        defender = m1
    
    #Select Randomly whether m1 or m2 is the initial attacker
    #to other is the initial definder
    
    print(attacker.getName()+" goes first. \n")
    #Loop until either 1 is unconscious or timeout
    while(m1.getHealth() > 0 and m2.getHealth() > 0):
        #Determine what move the monster makes
        #Probabilities:
        #   60% chance of standard attack
        #   20% chance of defense move
        #   20% chance of special attack move

        #Pick a number between 1 and 100
        move = random.randint(1,100)
        #It will be nice for output to record the damage done
        defenderhealth = defender.getHealth()
        attackerhealth = attacker.getHealth()
        
        #for each of these options, apply the appropriate attack and 
        #print out who did what attack on whom
        if(move >= 1 and move <= 60):
            #Attacker uses basic attack on defender
            attacker.basicAttack(defender)
            print(attacker.getName(), "used", attacker.basicName(), "on", defender.getName())
        elif move >= 61 and move <= 80:
            #Defend!
            attacker.defenseAttack(defender)
            print(attacker.getName(), "used", attacker.defenseName(), "on", defender.getName())
            #attack = attacker
            #defense = defender
            #attacker = defense
            #defender = attack
            
        else:
            #Special Attack!
            attacker.specialAttack(defender)
            print(attacker.getName(), "used", attacker.specialName(), "on", defender.getName())

        print(defender.getName(), "at", defenderhealth)
        print(attacker.getName(), "at", attackerhealth, "\n")

        #Swap attacker and defender
        attack = attacker
        defense = defender
        attacker = defense
        defender = attack    
        
        #Print the names and healths after this round
        #print(defender, "at", before_health)
        #print(attacker, "at", attacker.get_health())
    
    #Return who won
    if m1.getHealth() <= 0:
        return m2.getName()
    else:
        return m1.getName()

#----------------------------------------------------
if __name__=="__main__":
    #Every battle should be different, so we need to
    #start the random number generator somewhere "random".
    #With no input Python will set the seed
    
    i = random.randint(1, 100)
    
    random.seed(i)
    first = Pikachu("Pikachu")
    second = Thanos("Thanos")
    
    winner = monster_battle(first,second)
    
    #Print out who won
    print(winner, "is victorious!")
    