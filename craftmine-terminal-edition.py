import math
import time
import random
import os
import datetime
if not os.path.exists('C:\Users\andre\Downloads\Craftmine-Terminal-Edition-main\logs'):
    os.makedirs('C:\Users\andre\Downloads\Craftmine-Terminal-Edition-main\logs')
file = open(f'C:\Users\andre\Downloads\Craftmine-Terminal-Edition-main\logs\log_{datetime.now()}.txt', 'x')

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

# clear_terminal() just clears the terminal for better visuals
def clear_terminal():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# explore() is where the player has a random chance to find item(s), locations, or trigger an event
def explore():
    global wood, stone, inventory, exploreEventItems, exploreEvent, bread, wheat, iron
    if random.randint(1,6) == 1 and 'stone axe' in inventory:
        with open(f'C:\Users\andre\Downloads\Craftmine-Terminal-Edition-main\logs\log_{datetime.now()}.txt', 'a'):
            file.write(f"{datetime.now()}: tree chopped")
        exploreEventItems = random.randint(3,8)
        exploreEvent = "a tree"
        wood = wood + exploreEventItems
        exploreEventItems = f"got +{exploreEventItems} wood"
        done_exploring()
        return
    elif random.randint(1,8) == 1 and 'stone pick' in inventory:
        with open(f'C:\Users\andre\Downloads\Craftmine-Terminal-Edition-main\logs\log_{datetime.now()}.txt', 'a'):
            file.write(f"{datetime.now()}: rock mined")
        exploreEventItems = random.randint(2,5)
        exploreEvent = "a large rock"
        stone = stone + exploreEventItems
        exploreEventItems = f"got +{exploreEventItems} stone"
        done_exploring()
        return
    elif random.randint(1,12) == 1:
        with open(f'C:\Users\andre\Downloads\Craftmine-Terminal-Edition-main\logs\log_{datetime.now()}.txt', 'a'):
            file.write(f"{datetime.now()}: village found")
        exploreEventItems = random.randint(3,8)
        exploreEvent = 'village'
        bread = bread + exploreEventItems
        exploreEventItems = f"+{exploreEventItems} bread"
        done_exploring()
        return
    elif random.randint(1,12) == 1:
        if random.randint(1,6) == 1 and difficulty == 'n':
            if 'stone axe' in inventory:
                with open(f'C:\Users\andre\Downloads\Craftmine-Terminal-Edition-main\logs\log_{datetime.now()}.txt', 'a'):
                    file.write(f"{datetime.now()}: cave found, and attacked and defended")
                exploreEventItems = 'you got attacked by zombies and tried to defend yourself with your stone axe. -health'
                exploreEvent = 'a cave'
                health = health - random.randint(0,2)
                done_exploring()
                return
            else:
                with open(f'C:\Users\andre\Downloads\Craftmine-Terminal-Edition-main\logs\log_{datetime.now()}.txt', 'a'):
                    file.write(f"{datetime.now()}: cave found, and attacked")
                exploreEvent = 'a cave'
                exploreEventItems = 'you got attacked by zombies. -health'
                health = health - random.randint(1,3)
        else:
            with open(f'C:\Users\andre\Downloads\Craftmine-Terminal-Edition-main\logs\log_{datetime.now()}.txt', 'a'):
                file.write(f"{datetime.now()}: cave found with some iron")
            exploreEvent = 'a cave'
            exploreEventItems = 'mined some iron.'
            iron = iron + random.randint(0,5)
    else:
        if random.randint(1,3) == 1:
            with open(f'C:\Users\andre\Downloads\Craftmine-Terminal-Edition-main\logs\log_{datetime.now()}.txt', 'a'):
                file.write(f"{datetime.now()}: scraps found")
            wood = wood + random.randint(0,2)
            stone = stone + random.randint(0,1)
            wheat = wheat + random.randint(0,3)
            exploreEventItems = 'got some scraps from the ground'
            done_exploring()
            return
        else:
            with open(f'C:\Users\andre\Downloads\Craftmine-Terminal-Edition-main\logs\log_{datetime.now()}.txt', 'a'):
                file.write(f"{datetime.now()}: nothing happened")
            exploreEventItems = 'nothing happened'
        exploreEvent = 'nothing'
        done_exploring()
        return

# done_exploring() refers to when the 'explore' action finishes
def done_exploring():
    global exploreEvent, exploreEventItems, day
    print(f"You explored and found {exploreEvent} and {exploreEventItems}")
    # Reset exploreEventItems if needed
    exploreEventItems = ''
    day = day + 1
    # No call to main_loop here; let main_loop continue naturally
    pass

# main_loop() is the main game loop where most actions happen
def main_loop():
    global wood, stone, gold, inventory, action, craftingAction, exploreEventItems, bread, day, hunger, health, playAgain, exploreEvent, wheat, iron
    while True:
        if day == 100:
            print("You Survived, Congratulations!")
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
                main_loop()
                return
            elif playAgain == 'no' or playAgain == 'No':
                break
        exploreEventItems = ''
        if bread == 0:
            hunger = hunger + 1
        elif bread > 0:
            if hunger > 0:
                bread = bread - 1
                hunger = hunger - hunger
        if hunger > 0 and bread == 0:
            health = health - random.randint(1,2)
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
                main_loop()
                return
            elif playAgain == 'no' or playAgain == 'No':
                break
        print("")
        print("")
        print(f"Health:{health}")
        print(f"Hunger:{hunger}")
        print(f"Day:{day}")
        print("Resources:")
        print(f" Wood:{wood}")
        print(f" Gold:{gold}")
        print(f" Stone:{stone}")
        print(f" Bread:{bread}")
        print(f" Wheat:{wheat}")
        print("Inventory:")
        print(f" {inventory}")
        print("Type 'help' for a list of actions")
        action = input("What do you want to do? ")
        if action == 'give up':
            health = 0
        if action == 'craft':
            clear_terminal()
            print("Resources:")
            print(f" Wood:{wood}")
            print(f" Gold:{gold}")
            print(f" Stone:{stone}")
            print(f" wheat:{wheat}")
            print("stone axe: 2 wood + 2 stone")
            print("stone pick: 2 wood + 3 stone")
            print("bread: 3 wheat per")
            craftingAction = input("What do you want to craft? ")
            
            if craftingAction == 'stone axe':
                if stone >= 2 and wood >= 2:    
                    wood = wood - 2
                    stone = stone - 2
                    inventory = inventory + 'stone axe,'
                    day = day + 1
                    main_loop()
                    return
                else:
                    print("Not enough resources!")
                    day = day + 1
                    main_loop()
                    return
            elif craftingAction == 'stone pick':
                if stone >= 3 and wood >= 2:
                    wood = wood - 2
                    stone = stone - 3
                    inventory = inventory + 'stone pick,'
                    day = day + 1
                    main_loop()
                    return
                else:
                    print("Not enough resources!")
                    day = day + 1
                    main_loop()
                    return
            elif craftingAction == 'bread':
                if bread >= 3:
                    bread = math.floor(wheat/3)
                    wheat = wheat - math.floor(wheat/3) * 3
                    day = day + 1
                    main_loop()
                    return
                else:
                    print("Not enough resources!")
                    day = day + 1
                    main_loop()
                    return
        elif action == 'explore':
            explore()
        elif action == 'help':
            print("Actions include the following:")
            print(" help - brings up this menu")
            print(" explore - you explore for the day")
            print(" craft - you need to craft something")
            print(" give up - you decide to lose")
            print(" advanced resources - lists all the advance resources and how much of them you have")
            print(" difficulty - allows you to change the difficulty")
            print(" objective - displays how to beat the game")
            print(" nothing - you do nothing but rest, there's also a 1/3 chance you heal some")
            print(" Locations/Events + chances:")
            print("  Found scraps: 1/3")
            print("  Village: 1/12")
            print("  Tree: 1/6")
            print("  Rock: 1/8")
            print("  Nothing: everything else")
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
            print(f"Days remaining: {100 - day}")
        elif action == 'nothing':
            print("You decide to rest and do nothing for the day")
            if random.randint(1,3) == 1 and health < 12:
                health = health + random.randint(1,2)
                print("You gained back some health")
            day = day + 1
        else:
            print("You decide to rest and do nothing for the day")
            day = day + 1

main_loop()