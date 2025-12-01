import math
import time
import random
import os

# Variables to be defined when the program is ran
wood = 5
gold = 10
stone = 5
bread = 5
wheat = 0
iron = 0
hunger = 0
inventory = 'stone axe, stone pick,'
action = ''
craftingAction = ''
exploreEvent = ''
exploreEventItems = ''
day = 0
health = 12
difficulty = 'n'
dimension = 'overworld'
portalFound = 'false'
playAgain = ''
enterPortal = ''
clearDays = [3,6,8,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99]

# clear_terminal() just clears the terminal for better visuals
def clear_terminal():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# explore() is where the player has a random chance to find item(s), locations, or trigger an event
def explore():
    global wood, stone, inventory, exploreEventItems, exploreEvent, bread, wheat, iron, portalFound, dimension, health
    if dimension == 'overworld':
        # Tree event
        if random.randint(1,6) == 1 and 'stone axe' in inventory or 'iron axe' in inventory:
            exploreEventItems = random.randint(3,8)
            exploreEvent = "a tree"
            wood += exploreEventItems
            exploreEventItems = f"+{exploreEventItems} wood"
            done_exploring()
            return
        # Stone event
        elif random.randint(1,8) == 1 and 'stone pick' in inventory or 'iron pick' in inventory:
            exploreEventItems = random.randint(2,5)
            exploreEvent = "a large rock"
            stone += exploreEventItems
            exploreEventItems = f"+{exploreEventItems} stone"
            done_exploring()
            return
        # Village event
        elif random.randint(1,12) == 1:
            exploreEventItems = random.randint(1,3)
            exploreEvent = 'village'
            bread += exploreEventItems
            exploreEventItems = f"+{exploreEventItems} bread"
            done_exploring()
            return
        # Cave event
        elif random.randint(1,12) == 1:
            if random.randint(1,6) == 1 and difficulty == 'n':
                if 'stone axe' in inventory or 'iron axe' in inventory:
                    exploreEventItems = 'you got attacked by zombies and tried to defend yourself with your stone axe. -health'
                    exploreEvent = 'a cave'
                    health -= random.randint(0,2)
                    done_exploring()
                    return
                else:
                    exploreEvent = 'a cave'
                    exploreEventItems = 'you got attacked by zombies. -health'
                    health -= random.randint(1,3)
                    done_exploring()
                    return
            else:
                exploreEvent = 'a cave'
                exploreEventItems = 'mined some iron.'
                iron += random.randint(0,5)
                done_exploring()
                return
        elif random.randint(1,10) == 1:
            exploreEventItems = 'nothing else'
            exploreEvent = 'a portal'
            portalFound = 'true'
            done_exploring()
            return
        # Events for if nothing happens
        else:
            if random.randint(1,3) == 1:
                wood += random.randint(0,2)
                stone += random.randint(0,1)
                wheat += random.randint(0,3)
                exploreEvent = 'nothing'
                exploreEventItems = 'got some scraps from the ground'
                done_exploring()
                return
            else:
                exploreEventItems = 'nothing happened'
                exploreEvent = 'nothing'
                done_exploring()
                return
    elif dimension == 'hell':
        print("""
            This dimension has yet to be implemented! Please type 'portal' and confirm to leave hell.
            You can suggest things to add to it on the project's Github page:
            https://github.com/SimplyCodingStuff/Craftmine-Terminal-Edition
            Thanks!
            """)
        main_loop()
        return

# done_exploring() refers to when the 'explore' action finishes
def done_exploring():
    global exploreEvent, exploreEventItems, day
    print(f"You explored and found {exploreEvent} and {exploreEventItems}")
    # Reset exploreEventItems
    exploreEventItems = ''
    day += 1
    # No call to main_loop here; let main_loop() continue naturally
    pass

# main_loop() is the main game loop where most actions happen
def main_loop():
    global wood, stone, gold, inventory, action, craftingAction, exploreEventItems, bread, day, hunger, health, playAgain, exploreEvent, wheat, iron, dimension, portalFound, enterPortal, clearDays
    while True:
        if day in clearDays:
            clear_terminal()
        # The if statement below detects wether it's the final day (day 100) to see if the player should win
        if day == 100:
            print("You Survived, Congratulations!")
            print("""
            Thanks for playing! 
            Consider following me for more updates and projects at:
            https://github.com/SimplyCodingStuff
            """)
            playAgain = input("Play again?Yes/No ")
            if playAgain == 'yes' or playAgain == 'Yes':
                wood = 5
                gold = 10
                stone = 5
                bread = 5
                hunger = 0
                wheat = 0
                iron = 0
                inventory = 'stone axe, stone pick,'
                action = ''
                craftingAction = ''
                exploreEvent = ''
                exploreEventItems = ''
                day = 0
                health = 12
                playAgain = ''
                dimension = 'overworld'
                portalFound = 'false'
                enterPortal = ''
                main_loop()
                return
            elif playAgain == 'no' or playAgain == 'No':
                break
        exploreEventItems = ''
        # The next two if statements change the player's hunger and automatically consumes bread if hunger is greater than zero
        if bread == 0 or hunger == 0:
            hunger += 1
        elif bread > 0 and hunger > 0:
            bread = bread - 1
            hunger -= hunger
        if hunger >= 6 and bread == 0:
            health -= random.randint(1,2)
        # The if statement below detects wether the player is dead or should be dead every game loop
        if health <= 0:
            print("You died!")
            playAgain = input("Play again?Yes/No ")
            if playAgain == 'yes' or playAgain == 'Yes':
                wood = 5
                gold = 10
                stone = 5
                bread = 5
                hunger = 0
                wheat = 0
                iron = 0
                inventory = 'stone axe, stone pick,'
                action = ''
                craftingAction = ''
                exploreEvent = ''
                exploreEventItems = ''
                day = 0
                health = 12
                playAgain = ''
                dimension = 'overworld'
                portalFound = 'false'
                enterPortal = ''
                main_loop()
                return
            elif playAgain == 'no' or playAgain == 'No':
                break
        # The next bit displays the player's current stats and positions
        print(f"""
        Current Dimension:{dimension}
        Days remaining:{100 - day}
        Health:{health}
        Hunger:{hunger}
        Day:{day}
        Resources:
            Wood:{wood}
            Gold:{gold}
            Stone:{stone}
            Bread:{bread}
            Wheat:{wheat}
        Inventory:
            {inventory}
        Type 'help' for a list of actions
        """)
        action = input("What do you want to do? ")
        if action == 'give up':
            health = 0
        if action == 'craft':
            clear_terminal()
            print(f"""
            Resources:
                Wood:{wood}
                Gold:{gold}
                Stone:{stone}
                wheat:{wheat}
                iron:{iron}
            Tools:
                stone axe: 2 wood + 2 stone
                stone pick: 2 wood + 3 stone
                iron axe: 2 wood + 2 iron
                iron pick: 2 wood + 3 iron
            Foods:
                bread: 3 wheat per
            """)
            # The next few parts are the crafting system
            craftingAction = input("What do you want to craft? ")
            
            if craftingAction == 'stone axe':
                if stone >= 2 and wood >= 2:    
                    wood -= 2
                    stone -= 2
                    inventory = inventory + 'stone axe,'
                    day += 1
                    main_loop()
                    return
                else:
                    print("Not enough resources!")
                    day += 1
                    main_loop()
                    return
            elif craftingAction == 'stone pick':
                if stone >= 3 and wood >= 2:
                    wood -= 2
                    stone -= 3
                    inventory = inventory + 'stone pick,'
                    day += 1
                    main_loop()
                    return
                else:
                    print("Not enough resources!")
                    day += 1
                    main_loop()
                    return
            elif craftingAction == 'bread':
                if wheat >= 3:
                    bread = math.floor(wheat/3)
                    wheat = wheat - math.floor(wheat/3) * 3
                    day += 1
                    main_loop()
                    return
                else:
                    print("Not enough resources!")
                    day += 1
                    main_loop()
                    return
            elif craftingAction == 'iron pick':
                if iron >= 3 and wood >= 2:
                    iron -= 3
                    wood -= 2
                    inventory += ' iron pick,'
                    day += 1
                    main_loop()
                    return
            elif craftingAction == 'iron axe':
                if iron >= 2 and wood >= 2:
                    iron -= 3
                    wood -= 2
                    inventory += ' iron axe,'
                    day += 1
                    main_loop()
                    return
        # Explore action
        elif action == 'explore':
            explore()
        # Below is where the help menu is displayed
        elif action == 'help':
            print("""
            Actions include the following:
                help - brings up this menu
                explore - you explore for the day
                craft - you need to craft something
                give up - you decide to lose
                advanced resources - lists all the advance resources and how much of them you have
                difficulty - allows you to change the difficulty
                objective - displays how to beat the game
                nothing - you do nothing but rest, there's also a 1/3 chance you heal some
                portal - if you have found a portal then you can use this to enter and exit it
            Locations and Events + chances:
                Found scraps: 1/3
                Village: 1/12
                Tree: 1/6
                Rock: 1/8
                Nothing: everything else
            """)
        elif action == 'advanced resources':
            print(f"""
                Advanced Resources:
                    Iron:{iron}
            """)
        elif action == 'difficulty':
            print(f"Choose a difficulty. n=normal p=peaceful, current difficulty is '{difficulty}'")
            difficulty = input("New Difficulty: ")
            pass
        elif action == 'objective':
            print("Your objective is to survive 100 days")
        elif action == 'nothing':
            print("You decide to rest and do nothing for the day")
            if random.randint(1,3) == 1 and health < 12:
                health += random.randint(1,2)
                print("You gained back some health")
            day += 1
        elif action == 'portal':
            if portalFound == 'true':
                if dimension == 'overworld':
                    enterPortal = input("Do you want to enter the portal? y/n ")
                    if enterPortal == 'y' or enterPortal == 'Y' or enterPortal == 'yes' or enterPortal == 'Yes':
                        dimension = 'hell'
                        print("You decided to enter the portal and enter hell.")
                        clear_terminal()
                        main_loop()
                        return
                    elif enterPortal == 'no' or enterPortal == 'No' or enterPortal == 'n' or enterPortal == 'N':
                        print("You decided not to enter the portal.")
                        clear_terminal()
                        main_loop()
                        return
                    else:
                        print("Not a valid input!")
                        clear_terminal()
                        main_loop()
                        return
                elif dimension == 'hell':
                    enterPortal = input("Do you want to enter the portal and leave hell? y/n ")
                    if enterPortal == 'y' or enterPortal == 'Y' or enterPortal == 'yes' or enterPortal == 'Yes':
                        dimension = 'overworld'
                        print("You decided to enter the portal and leave hell.")
                        main_loop()
                        return
                    elif enterPortal == 'no' or enterPortal == 'No' or enterPortal == 'n' or enterPortal == 'N':
                        print("You decided not to enter the portal.")
                        main_loop()
                        return
                    else:
                        print("Not a valid input!")
                        main_loop()
                        return
            else:
                print("You have not found the portal so you cannot enter it.")
                main_loop()
                return
        else:
            print("You decide to rest and do nothing for the day")
            day += 1
# End of the main game loop
print("Welcome to Craftmine: Terminal Edition!")
main_loop()