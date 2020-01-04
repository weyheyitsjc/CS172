from monster import monster

class HandsomeSquidward(monster):
    def __init__(self,name):
        self.__name = name
        self.__health = 50
        
    def __str__(self):
        return ""
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return "The defintion of sexy"
    
    def basicAttack(self,enemy):
        return enemy.doDamage(-10)
    
    def basicName(self):
        return "Too Sexy For My Sexy"
    
    def defenseAttack(self,enemy):
        return enemy.doDamage(0)
        
    def defenseName(self):
        return "I Get More Sexy!"
        
    def specialAttack(self,enemy):
        return enemy.doDamage(-30)
        
    def specialName(self):
        return "The machinations of my mind are an enigma"
    
    def getHealth(self):
        return self.__health

    def doDamage(self,damage):
        self.__health += damage
        return self.__health

    def resetHealth(self):
        self.__health = 50
        return self.__health
        
    
class Thanos(monster):
    def __init__(self,name):
        self.__name = name
        self.__health = 50
        
    def __str__(self):
        return ""
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return "The end is near"
    
    def basicAttack(self,enemy):
        return enemy.doDamage(-30)
    
    def basicName(self):
        return "Fun isn’t something one considers when balancing the universe. But this… does put a smile on my face"
    
    def defenseAttack(self,enemy):
        return enemy.doDamage(0)
        
    def defenseName(self):
        return "You should have gone for the head"
        
    def specialAttack(self,enemy):
        return enemy.doDamage(-100)
        
    def specialName(self):
        return "When I’m done, half of humanity will still exist. Perfectly balanced, as all things should be. I hope they remember you"
    
    def getHealth(self):
        return self.__health

    def doDamage(self,damage):
        self.__health += damage
        return self.__health

    def resetHealth(self):
        self.__health = 100
        return self.__health
        