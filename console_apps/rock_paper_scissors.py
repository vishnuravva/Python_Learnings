import random

def machineDecision(play):
    return random.choice(play)
print("Provide moves to play")
moves = int(input())
i = 0
play = ["rock","paper","scissor"]
computerScore = 0
userScore = 0
while(i < moves):
    print("Select rock, paper, scissor")
    userMove = input()
    
    print("Your move: " + userMove)
    if userMove not in play:
        print("Inalid move, try again.\n")
        continue
    else:
        computerDecision = machineDecision(play)
        print("Computer move: " + computerDecision)
        if computerDecision == "rock" and (userMove == "scissor"):
            computerScore+=1
        elif(computerDecision == "scissor" and userMove == "paper"):
            computerScore+=1
        elif computerDecision == "paper" and userMove == "rock":
            computerScore +=1 
        elif(userMove == "rock" and computerDecision == "scissor"):
            userScore+=1
        elif(userMove == "scissor" and computerDecision == "paper"):
            userScore+=1
        elif(userMove == "paper" and computerDecision == "rock"):
            userScore+=1    
        i+=1

print("User Score: ",userScore)
print("Computer Score: ",computerScore)

if userScore > computerScore:
    print("Hurray you won")
elif userScore == computerScore:
    print("Tied between you and computer")
else:
    print("Cmnputer won")