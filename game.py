import random
import time
chosenPath = 1
# global correctPath
correctPath = 0
def displayIntro():
    print("North Korea, The USA, one giant war")
    print("North Korea has 11 nuclear weapons")
    print("USA hsa over 750,000 soldiers ")
    print("USA also has 35,000 troops on the border between South Korea")
    print("Perks on the way are available")
    print("USA has less power but an excessive amount of soldiers")
    print("North Korea has a very slow firing rate but more power")
    print("Each team starts with 500 health plus any shield held")
    print("Which team will you choose in the ultimate throw down of USA vs NK")
    

def choosePath0path = ""
    while path != "USA" and path != "North Korea": 
        path = input("Which Country Do You Go Down With? (NK or USA): ")

    return path

def checkPath(choice, correctPath):
    if choice == "North Korea":
        print("One nuclear bomb ready to fire")
        time.sleep(2)
        print("Fire in the hole")
        time.sleep(2)
        print("Reports are in.. Kim Jun Un, thats a miss on the bomb")
        time.sleep(2)
        print("Keep realoading we need to destroy this iggnorant country")
        time.sleep(2)
        print("Miss again")
        time.sleep(2)
        print("I am just going to keep hitting the button then!!")
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
