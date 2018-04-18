import random
import time
chosenPath = 1
# global correctPath
correctPath = 0
def displayIntro():
    print("North Korea vs. The United States of America")
    print("North Korea has nuclear weapons, USA has soldiers and shield held")
    print("You can pick up multiple different perks along the way")
    print("USA has less power but multiple people")
    print("North Korea has a very slow firing rate but more power")
    print("Each team starts with 500 health plus any shield held")
    print("Which team will you choose in the ultimate throw down of USA vs NK")
    

def choosePath():
    path = ""
    while path != "Home" and path != "Island": 
        path = input("Which Country Do You Go With? (North Korea or USA): ")

    return path

def checkPath(choice, correctPath):
    if choice == "North Korea":
        print("One nuclear bomb ready to fire")
        time.sleep(2)
        print("Fire in the hole")
        time.sleep(2)
        print("Reports are in.. Kim Jun Un, thats a miss on the bomb")
        time.sleep(2)
        print("Keep realoading we need to hit these damn people")

    if choice == "USA":
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
    choice = choosePath()  #######
    checkPath(choice, correctPath) 
    ans = input("Do you want to play again? (yes or y to continue playing): ")
    count += 1
    if ans == 'yes':
        playAgain = False
    if ans == 'y':
        playAgain = False
    if count > 3:
        playAgain = False
