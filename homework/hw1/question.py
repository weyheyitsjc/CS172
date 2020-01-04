class Questions:
    def __init__(self, question = "", a = "", b = "", c = "", d = "", answer = ""): #attributes of object
        self.question = question
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.answer = answer
        
    def __str__(self): #creates string of question and options to be printed
        mystr = str(self.question) + "\n" + str(self.a) + "\n" + str(self.b) + "\n" + str(self.c) + "\n" + str(self.d)
        return mystr
    
    def getAnswer(self): #getter method, gets the correct answer
        return self.answer