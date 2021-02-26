import random

def checkIfNumber(user_guess):
    if (user_guess.isnumeric()):
        return True
    else:
        print("The number that you have entered is not a valid number.")
        return False

def checkIfInRange(user_guess):
    if( (1 <= user_guess) and (user_guess <= 100)):
        return True
    else:
        print("The number you have entered is not in the 1-100 range, please try again")
        return False 


def getValidValue():
    while(True):
        UserGuess = input("Please guess a number in range from 1 to 100: ")
        if(checkIfNumber(UserGuess)):
            UserGuess = int(UserGuess)
            if(checkIfInRange(UserGuess)):
                return UserGuess

def main():
    SavedNumber = random.randint(1, 100)
    NumberOfSteps = 0
    UserGuess = 0

    while(UserGuess != SavedNumber):
        UserGuess = getValidValue()

        if(SavedNumber == UserGuess): 
            print("You are the winner! After ", NumberOfSteps, "steps")
        elif(SavedNumber > UserGuess):
            print("The number is too small")
            NumberOfSteps = NumberOfSteps + 1
        else:
            print("The number is too big")
            NumberOfSteps = NumberOfSteps + 1 
    print("Goodbye")  

main()
