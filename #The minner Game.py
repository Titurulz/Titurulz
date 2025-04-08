# Write code below 💖
#The minner Game

#this game is about to selling resources
#You start the game with 100€ and 0 resources
#You have to buy TnT to mine resources
#You can sell the resources to make money


import random


#Character
character_name = "Tim"
character_money = 100
character_tnt = 0
character_big_tnt = 0
character_cooper = 0
character_silver = 0
character_gold = 0
character_safire = 0
character_diamond = 0

def character_resources ():
  return character_cooper + character_silver + character_gold + character_safire + character_diamond

#Prices

#Bombs
TNT = 10
Big_TNT = 25

#Resources
Cooper = 5
Silver = 10
Gold = 20
Safire = 50
Diamond = 100

#Rounds
rounds = 30

#Game
#Main loop

start_game = True

while start_game and rounds > 0:
    print("Welcome to the miner game")
    print(f"You have {character_money}€ and {character_resources()} resources")
    print("You can buy TNT to mine resources")
    print("You can sell the resources to make money")
    print("You can buy TNT or Big TNT,"
    "you can get more resouces with Big TNT")

    print("What do you want to do?")

    print("1. Buy TNT")
    print("2. Buy Big TNT")

    print("3. Mine resources")
    print("4. Sell resources")
    
    print("5. Exit")

    
    action_choice = int(input("Enter your choice: "))

    if action_choice == 1:
        character_tnt += 1
        character_money -= TNT
        print("You bought TNT")
        print("You have now " + str(character_tnt) + " TNT")
        rounds -= 1

    if action_choice == 2:
        character_big_tnt += 1
        character_money -= Big_TNT
        print("You bought Big TNT")
        print("You have now " + str(character_big_tnt) + " Big TNT")
        rounds -= 1

    if action_choice == 3:
        print("Choose which TNT you want to use")
        print("1. TNT")
        print("2. Big TNT")

        tnt_choice = int(input("Enter which Boom Boom Power you want to use: "))

        if tnt_choice == 1 and character_tnt > 0:
            resources = random.choice(["Cooper", "Silver"])
            if resources == "Cooper":
                character_cooper += 1
            elif resources == "Silver":
                character_silver += 1
            character_tnt -= 1
            print(f"You mined {resources}")
            print("You have now " + str(character_resources()) + " resources")
        elif tnt_choice == 2 and character_big_tnt > 0:
            resources = random.choice(["Cooper", "Silver", "Gold", "Safire", "Diamond"])
            if resources == "Cooper":
                character_cooper += 1
            elif resources == "Silver":
                character_silver += 1
            elif resources == "Gold":
                character_gold += 1
            elif resources == "Safire":
                character_safire += 1
            elif resources == "Diamond":
                character_diamond += 1
            character_big_tnt -= 1       
            print(f"You mined {resources}")
            print("You have now " + str(character_resources()) + "resources")

        else:
            print("You don't have enought enought Boom Power")

        rounds -= 1

    if action_choice == 4:
        print("You have these resources")
        print(f"Cooper -> {character_cooper} {Cooper}€")
        print(f"Silver -> {character_silver} {Silver}€")
        print(f"Gold -> {character_gold} {Gold}€")
        print(f"Safire -> {character_safire} {Safire}€")
        print(f"Diamond -> {character_diamond} {Diamond}€")
        print("What do you want to sell?")
        print("1. Cooper")
        print("2. Silver")
        print("3. Gold")
        print("4. Safire")
        print("5. Diamond")
        print("6. All resources")

        sell_choice = int(input("Enter your choice: "))

        if sell_choice == 1 and character_cooper > 0:
            print("How much do you want to sell?")
            print("1. Just one?")
            print("2. All?")
            sell_amount_choice = int(input("Enter your choice: "))
            if sell_amount_choice == 1:
                character_money += Cooper
                character_cooper -= 1
                print("You sold one cooper")
            elif sell_amount_choice == 2:
                character_money += Cooper * character_cooper
                character_cooper = 0
                print("You sold all cooper")    
            if character_cooper == 0:
                print("You don't have any cooper left")
            else:
                print("Invalid choice")

        if sell_choice == 2 and character_silver > 0:
            print("How much do you want to sell?")
            print("1. Just one?")
            print("2. All?")
            sell_amount_choice = int(input("Enter your choice: "))
            if sell_amount_choice == 1:
                character_money += Silver
                character_silver -= 1
                print("You sold one silver")
            elif sell_amount_choice == 2:
                character_money += Silver * character_silver
                character_silver = 0
                print("You sold all silver")    
            if character_silver == 0:
                print("You don't have any silver left")
            else:
                print("Invalid choice")         

        if sell_choice == 3 and character_gold > 0:
            print("How much do you want to sell?")
            print("1. Just one?")
            print("2. All?")
            sell_amount_choice = int(input("Enter your choice: "))
            if sell_amount_choice == 1:
                character_money += Gold
                character_gold -= 1
                print("You sold one gold")
            elif sell_amount_choice == 2:
                character_money += Gold * character_gold
                character_gold = 0
                print("You sold all gold")    
            if character_gold == 0:
                print("You don't have any gold left")
            else:
                print("Invalid choice")
            
            
        if sell_choice == 4 and character_safire > 0:
            print("How much do you want to sell?")
            print("1. Just one?")
            print("2. All?")
            sell_amount_choice = int(input("Enter your choice: "))
            if sell_amount_choice == 1:
                character_money += Safire
                character_safire -= 1
                print("You sold one safire")
            elif sell_amount_choice == 2:
                character_money += Safire * character_safire
                character_safire = 0
                print("You sold all safire")    
            if character_safire == 0:
                print("You don't have any safire left")
            else:
                print("Invalid choice")
            

        if sell_choice == 5 and character_diamond > 0:
            print("How much do you want to sell?")
            print("1. Just one?")
            print("2. All?")
            sell_amount_choice = int(input("Enter your choice: "))
            if sell_amount_choice == 1:
                character_money += Diamond
                character_diamond -= 1
                print("You sold one diamond")
            elif sell_amount_choice == 2:
                character_money += Diamond * character_diamond
                character_diamond = 0
                print("You sold all diamond")    
            if character_diamond == 0:
                print("You don't have any diamond left")
            else:
                print("Invalid choice")

            
        if sell_choice == 6:
            character_money += (Cooper * character_cooper) + (Silver * character_silver) + (Gold * character_gold) + (Safire * character_safire) + (Diamond * character_diamond)
            character_cooper = 0
            character_silver = 0
            character_gold = 0
            character_safire = 0
            character_diamond = 0
            print("You sold all resources")

    rounds -= 1        

    #Quit game    
    
    if action_choice == 5:
        print("Thanks for playing!")
        rounds = 0
        start_game = False
        break


    #Loop's end
    if rounds <= 0:
        print("This is the end, for now. Hope that you enjoyed the gameplay."
              "Thank you")
        break
        

input("\nPress Enter to exit the game...")
