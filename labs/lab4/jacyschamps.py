from monster import monster

class Bunny(monster):
    def __init__(self, name):
        self.__name = name
        self.__health = 50
    
    def __str__(self):
        #mystr = self.__name + ": " + self.getDescription()
        #return mystr
        return ""
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return "The cute but deadly bunny."
    
    def basicAttack(self,enemy):
        return enemy.doDamage(-5)
        
    def basicName(self):
        attack = "Bite"
        return attack
    
    def defenseAttack(self,enemy):
        return enemy.doDamage(0)
        
    def defenseName(self):
        defense = "Hide"
        return defense
    
    def specialAttack(self,enemy):
        return enemy.doDamage(-15)
        
    def specialName(self):
        special = "Ravenous Fury"
        return special
    
    def getHealth(self):
        return self.__health
    
    def doDamage(self, damage):
#        import pdb
#        pdb.set_trace()
         self.__health = self.__health + damage
         return self.__health
        
    def resetHealth(self):
        self.__health = 50
        return self.__health
        
class Pikachu(monster):
    def __init__(self, name):
        self.__name = name
        self.__health = 50
    
    def __str__(self):
        #mystr = self.__name + ": " + self.getDescription()
        #return mystr
        return ""
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return "The cute but deadly Pokemon"
    
    def basicAttack(self,enemy):
        return enemy.doDamage(-7)
        
    def basicName(self):
        return "Thunder Shock"
    
    def defenseAttack(self,enemy):
        return enemy.doDamage(-1)
        
    def defenseName(self):
        return "Double Kick"
    
    def specialAttack(self,enemy):
        return enemy.doDamage(-15)
        
    def specialName(self):
        return "Thunder"
    
    def getHealth(self):
        return self.__health
    
    def doDamage(self, damage):
        self.__health = self.__health + damage
        return self.__health
        
    def resetHealth(self):
        self.__health = 50
        return self.__health