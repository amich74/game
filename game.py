import random
import time
chosenPath = 1
# global correctPath
correctPath = 0
def displayIntro():
    print("It is the end of a long deployment in these waters")
    print("You come to two paths on your trip back to base one path leads home")
    print("where you will be handsomly rewarded for a job well done")
    print("and the other leads to a island with a brand new start")
    print("where you wont regret whats happening, new house and a new friend")

def choosePath():
    path = ""
    while path != "Home" and path != "Island": 
        path = input("Which path will you choose? (Home or Island): ")

    return path

def checkPath(choice, correctPath):
    if choice == "Island":
        print("You head down the path")
        time.sleep(2)
        print("there's an island near by that looks weird, I am scared")
        time.sleep(2)
        print("But your skin begins to tingle...")
        time.sleep(2)
        print("I am going to go explore, don't worry people I have my gun with me")
        correctPath = random.randint(1, 2)

    if chosenPath == correctPath:
        print("That tingling was just the feeling of nervousness")
        print("Welcome home!")
    else:
        print("An extremely energetic burst of gamma rays pass through you")
        print("causing all of the energy in your body to explode")
        print("there is no record left of any island")

count = 0 
playAgain = True
while playAgain:    
    displayIntro()
    choice = choosePath()
    checkPath(choice, correctPath) 
    ans = input("Do you want to play again? (yes or y to continue playing): ")
    count += 1
    if ans == 'yes':
        playAgain = False
    if ans == 'y':
        playAgain = False
    if count > 3:
        playAgain = False
