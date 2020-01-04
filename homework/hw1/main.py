from question import Questions
import random

print("Welcome to the Python intro programming quiz")
print("--------------------------------------------")

questionsList = [ #questions list - instantiates each questions with options and correct answers as an object
    Questions("What is the chemical element represented by 'W'?",
              "a. Tungsten", "b. Potassium", "c. Bohrium", "d. Lead",
              "a"),
    Questions("The beaver is the national emblem of which country?",
              "a. USA", "b. Canada", "c. Russia", "d. UK",
              "b"),
    Questions("How many players are there in a baseball team?",
              "a. 9", "b. 11", "c. 8", "d. 15",
              "a"),
    Questions("In Fahrenheit, at what temperature does water freeze?",
              "a. 20 degrees", "b. 0 degrees", "c. 32 degrees", "d. 7 degrees",
              "c"),
    Questions("Who was the US president during World War I?",
              "a. Woodrow Wilson", "b. Barack Obama", "c. Dwight Eisenhower", "d. Harry Truman",
              "a"),
    Questions("Which US city is known as the City of Brotherly Love?",
              "a. Boston", "b. Philadelphia", "c. Chicago", "d. New York",
              "b"),
    Questions("Who is Simba's (from the Lion King) evil uncle?",
              "a. Tom", "b. Jafar", "c. Prince Hands", "d. Scar",
              "d"),
    Questions("Where is the smallest bone in the body?",
             "a. pinky toe", "b. finger", "c. ear", "d. mouth (teeth)",
             "c"),
    Questions("What is the largest ocean?",
             "a. Atlantic", "b. Pacific", "c. Artic", "d. Indian",
             "b"),
    Questions("Where do orange trees originally come from?",
             "a. China", "b. Florida", "c. California", "d. Spain",
             "a")
    ]

random.shuffle(questionsList) #shuffles questions
player = 1
player1Score = 0
player2Score = 0
correctLetters = "abcd"

for i in range(0, len(questionsList)):
    '''
    for loop runs through all the questions changing players each time until all questions are played
    '''
    if player == 1: #check if player 1 - player 1's turn
        print("Player 1 here is your question:")
        print(str(questionsList[i]))
        print()
        answer = input("Enter your answer:\n")
        while player == 1: #check the answer player1 inputed
            if answer.lower() == questionsList[i].getAnswer(): #correct answer
                player1Score += 1
                print("Excellent answer! You score!\n")
                player = 2
            elif answer.lower() != questionsList[i].getAnswer():
                if answer.lower() in correctLetters: #incorrect answer
                    print("This is incorrect. Better luck with the next question.\n")
                    player = 2
                else: #not a,b,c,d - asks for another answer
                    print("Error: your answer has to be a letter between a and c. Try again.")
                    answer = input("Enter your answer:\n")
    elif player == 2: #check if player 2 - player 2's turn
        print("Player 2 here is your question:")
        print(str(questionsList[i]))
        print()
        answer = input("Enter your answer:\n")
        while player == 2: #check the answer player2 inputed
            if answer.lower() == questionsList[i].getAnswer(): #correct answer
                player2Score += 1
                print("Excellent answer! You score!\n")
                player = 1
            elif answer.lower() != questionsList[i].getAnswer():
                if answer.lower() in correctLetters: #incorrect answer
                    print("This is incorrect. Better luck with the next question.\n")
                    player = 1
                else: #not a,b,c,d - asks for another answer
                    print("Error: your answer has to be a letter between a and c. Try again.")
                    answer = input("Enter your answer:\n")
                
print("And the final scores are:") #printing scores, winner, etc.
print("Player 1:", player1Score)
print("Player 2:", player2Score)

if player1Score > player2Score:
    print("Player 1 wins!\n")
elif player1Score == player2Score:
    print("It's a tie!\n")
else:
    print("Player 2 wins!\n")
    
print("Thank you for playing! :)")