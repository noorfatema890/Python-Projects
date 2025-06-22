'''
Galaxy Tour Game is a space adventure where you explore planets, 
manage resources (fuel, oxygen, food), 
and meet aliens. Fight enemies, trade, 
and collect items,
and survive random space events. 
See how far you can travel!
'''


import random 

#initializing products
resources = {'fuel':100 , 'oxygen':100 , 'food':100}
ship_stat = {'gun':100 , 'shield':100}

#list of aliens
aliens = ['AL. Merchants' ,'AL. Zaalim' , 'AL. Neutral']

#visited planets (nested)
visited_planets = [['home planet','safe']]

#random events that may occur
random_events=[
    "found an abandoned spaceship with resources",
    "encountered a space storm",
    "discovered a new alien species",
    "your navigation system malfunctioned"
]

inventory = []

print('══════════════════ Welcome to Galaxy tour game ══════════════════')

def galaxytour():
    while True:
        print("\nGalactic Expedition Menu:")
        print("    1. Explore Planet")
        print("    2. Check Resources")
        print("    3. Check Ship Status")
        print("    4. View Inventory")
        print('    5. Visit new planet')
        print("    6. Check visited planets")
        print("    7. Exit")
        

        choice = input('\nYour choice: ')
        if choice == '1':
            explore()
        elif choice == '2':
            print('── .✦·········────')
            print('Your current resources are: ')
            #for resource,quantity in resources.items():
            [print(f"    {resource} : {quantity}") for resource,quantity in resources.items()]
        elif choice == '3':
            print('── .✦·········────')
            print('Ship Status:')
            #for item ,quantity in ship_stat.items():
            [print(f"    {item} : {quantity}") for item ,quantity in ship_stat.items()]
        elif choice == '7':
            print('\n── ⋆⋅☆⋅⋆ ── Game Ended ── ⋆⋅☆⋅⋆ ──')
            break
        elif choice == '5':
            print('── .✦·········────')
            while True:
                another_planet = input('Do you want to visit another planet? ').lower()
                if another_planet == 'yes':
                    name_of_planet = input('\nEnter planet you want to visit: ')
                    visit_planet(name_of_planet)
                elif another_planet == 'no':
                    print('No worries! lets move to other thing')
                    break
                else:
                    print("⚠ Invalid Choice ⚠. Please enter 'yes' or 'no'.")


        elif choice == '4':
            print("\nInventory")
            [print(f"  -{item}") for item in inventory]
            print('── .✦·········────')
        elif choice == '6':
            print(f"\nYou visited following planets: ")
            #[print(f" - {planet[0]} ({planet[1]})") for planet in visited_planets]
            print(visited_planets)
            print('── .✦·········────')
        else:
            print("⚠︎ Invalid Choice ⚠︎")

def visit_planet(planet):
        print('── .✦·········────')
        print(f'\nYou visited {planet}')
        specificity = random.choice(['Safe','Dangerous'])
        visited_planets.append([planet,specificity])
        if random.random() < 0.3:
            print('Oh no! You tripped over a stone and fell.')
            print('\n------> OXYGEN LEAK DETECECTED !!!')
            resources['oxygen'] -= 10
            print('── .✦·········────')
            inp = input('Hurry up! Type Fix to stop leaking')
            if inp.lower() == 'fix':
                print("\n✅ You sealed the leak! Oxygen stabilized.")
                print('\nRemaining Oxygen: ')
                print(f'\nRemaining Oxygen: {resources["oxygen"]}%')
            else:
                print('⚠︎ Invalid Choice ⚠︎')
            print('── .✦·········────')
        

def explore():
    if random.random() < 0.5:
        event = random.choice(random_events)
        print(f"╭──────────.★..─╮\n  Special Event\n╰─..★.──────────╯\n {event}")
        print()
        if 'found' in event:
            new_item = random.choice(['Crystal', 'Artifact', 'Map'])
            inventory.append(new_item)
            print(f"╰┈➤˗ˏˋFab!! You found {new_item}. ----added to inventory")
        elif "storm" in event:
            print("⚡ ⚡ You lost some of your resources")
            lost = random.choice(['fuel','oxygen'])
            amount = random.randint(10,30)
            resources[lost] -= amount
            print(f"You lost {amount} {lost}")
            print("\nRemaining Resources:")
            [print(f" -{resource}: {amount}") for resource,amount in resources.items()]
        elif "system" in event:
            print("⚠️ Critical system malfunction!")
            affected_system = random.choice(['gun', 'shield'])
            ship_stat[affected_system] -= 10
            print(f"{affected_system}% efficiency reduced!")
        elif "alien" in event:
            encounter_alien()
    elif random.random() < 0.5:
            encounter_alien()
    print('── .✦·········────')

def encounter_alien():
    print('── .✦·········────\n')
    alien = random.choice(aliens)
    print(f"You've encountered {alien}")

    if alien == 'AL. Merchants':
        print("They offer to trade resources with you.")
        trade()
    elif alien == 'AL. Zaalim':
        print("They're attacking your ship!")
        battle()
    elif alien == 'AL. Neutral':
        print("They're neutral, but might offer information.")
        neutral()

def trade():
    print('\n── .✦·········────')
    print('Trade Menu: ')
    print("1. Trade Fuel for Oxygen")
    print("2. Trade Food for Fuel")
    print("3. Decline Trade")

    choice = input('Enter Choice: ')
    if choice == '1':
        resources['fuel'] -= 10
        resources['oxygen'] +=10
        print('++Oxygen')
    elif choice == '2':
        resources['food'] -= 10
        resources['fuel'] +=10
        print('++fuel')
    elif choice == '3':
        print('Trade Declined')
    else:
        print("⚠︎ Invalid Choice ⚠︎")

def battle():
    print('\n── .✦·········────')
    print("Battle Menu: ")
    print("1. Engage Shields")
    print("2. Attack Alien")
    print("3. Retreat")

    choice = input('Enter Choice: ')
    if choice == '1':
        ship_stat['shield'] -= 20
        print("⛊⛉ Shields engaged! ⛊⛉")
    elif choice == '2':
        ship_stat['gun'] -= 20
        print('🗡🛡️ Alien Defeated 🗡🛡️')
        item = random.choice(['Alien tech blueprint','Black-hole key','celestial gun','shield booster'])
        if 'tech' in item:
            print(">>> ──────── .✦➤ You found Alien tech blueprint.")
            inventory.append('Alien tech blueprint')
        elif 'key' in item:
            print(">>> ──────── .✦➤ You found Black-hole key.")
            inventory.append('Black-hole key')
        elif 'gun' in item:
            print(">>> ──────── .✦➤ You found celestial gun ----- Increased gun efficiency.")
            ship_stat['gun'] +=25
        elif 'shield' in item:
            print(">>> ──────── .✦➤ You found shield booster----- Increased shield efficiency.")
            ship_stat['shield'] +=25
        
    elif choice == '3':
        print('Retreating....')
    else:
        print("⚠︎ Invalid Choice ⚠︎")

def neutral():
    print('── .✦·········────')
    print("\nAL. Neutral offer information about a nearby planet.")
    print("Do you want to visit the planet?")
    choice = input().lower()

    if choice == 'yes':
        print('── .✦·········────')
        print('Yay! You visited a planet a found some resources')
        resources['fuel'] += 20
        resources['oxygen'] +=20
        print('\nSo your current resources now are: ')
        #for i,j in resources.items():
        [print(f'{i} : {j}') for i,j in resources.items()]
        print('── .✦·········────')
        if random.random() < 0.5:
            print('Oh no! A bear scared you')
            print('You lost one of your item')
            if len(inventory) != 0:
                lost_item = inventory.pop(0)
                print(f'-----> You lost {lost_item}')
            else:
                print('No item in inventory')
    elif choice == 'no':
        print("You declined the offer.")
    else:
        print("⚠︎ Invalid Choice ⚠︎")



galaxytour()