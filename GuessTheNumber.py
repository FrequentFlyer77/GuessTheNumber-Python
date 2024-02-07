import random
import sys
def guess():
    am = True
    print("Please take a look at the readme file included in the package! It has the instructions and terms.")
    print("Type the following phrase strawberries when your ready!")
    inputLicense = input()
    inputLicense = inputLicense.lower()
    while am:
        if (inputLicense == "strawberries"):
            print("Pick a mode, (Easy, Normal, Hard, Insane): ")
            gameMode = input()
            gameMode = gameMode.lower()
            if (gameMode == "easy"):
                num = 10
            elif (gameMode == "normal"):
                num = 100
            elif (gameMode == "hard"):
                num = 1000
            elif (gameMode == "insane"):
                num = 1000000
            else:
                print("You didn't specify a mode!")
                print("Cancelled game!")
                return None
            print("Type ready when your ready!")
            readycheck = "no"
            while readycheck != "ready":
                readycheck = input()
        else:
            print("You didn't type the verification code!")
            print("Cancelled game!")
            return None
        numberExpected = random.randint(1,num)
        numberInput = 0
        numStr = str(num)
        while numberInput != numberExpected:
            print("Guess the number from 1 to " + numStr + ":")
            numberInput = input()
            numberInput = int(numberInput)
            if (numberInput < numberExpected):
                print("The number is higher!")
            elif (numberInput > numberExpected):
                print("The number is lower!")
        print("You won! Do you want to play again?")
        ao = "nonecurrently"
        while ao != "yes":
            ao = input()
            if ao == "yes":
                am = True
            elif ao == "no":
                return 0;
            else:
                am = False
                print("Please pick Yes or No.")
guess()




