print("Initializing...")

from colorama import Fore
import time
import random
from attack import PooCannon, DiarrheaHurricane, VomitCloud

bot1health = 150
bot2health = 150
Player1 = "Player 1, "
Player2 = "Player 2, "

time.sleep(1.75)

print(Fore.LIGHTYELLOW_EX + "\n CombatBots")
print(
    Fore.RED + "\n Directions: \n \t 1. The bot score must be under 200 - if it's not, the system will ask you what power to subtract from \n \t 2. 2 players need to create their own bots to battle \n \t 3. Have fun")


class Bot1:
    def __init__(self):
        self.agility = int(input(Fore.GREEN + "What should be your bot's agility?"))
        self.strength = int(input(Fore.GREEN + "What should be your bot's strength?"))
        self.speed = int(input(Fore.GREEN + "What fast should your bot's be?"))


class Bot2:
    def __init__(self):
        self.agility = int(input(Fore.GREEN + "What should be your bot's agility?"))
        self.strength = int(input(Fore.GREEN + "What should be your bot's strength?"))
        self.speed = int(input(Fore.GREEN + "What fast should your bot's be?"))


print(Fore.BLUE + "Player 1, create your bot!!")
BotOne = Bot1()
Bot1Total = BotOne.agility + BotOne.strength + BotOne.speed
print(Fore.BLUE + "Player 2, your turn!")
BotTwo = Bot2()
Bot2Total = BotTwo.agility + BotTwo.strength + BotTwo.speed


def rem_value(Bot, BotTotal, player):
    if BotTotal > 200:
        rm_from = input(Fore.RED + "Which value should we remove from? (" + player + "excess amount of points) ")
        if rm_from.lower() == "agility":
            new_agility = abs(200 - Bot.strength - Bot.speed)
            Bot.agility = new_agility
        elif rm_from.lower() == "strength":
            new_strength = abs(200 - Bot.agility - Bot.speed)
            Bot.strength = new_strength
        elif rm_from.lower() == "speed":
            new_speed = abs(200 - Bot.agility - Bot.strength)
            Bot.speed = new_speed
        else:
            print(Fore.RED + "You must enter a valid power")
            return quit()


rem_value(BotOne, Bot1Total, Player1)
rem_value(BotTwo, Bot2Total, Player2)

print(Fore.MAGENTA + "\n BATTLE TIME!")

attack = random.randrange(1, 5)


def attack(atk_bot, atk_bot_str, atk_bot_spd, dfn_bot_agl, dfn_bot_spd, dfn_bot_health, atk_bot_health):
    global bot1health, bot2health
    if atk_bot == BotOne:
        atk_bot_print = "Bot 1"
        dfn_bot_print = "Bot 2"
    else:
        atk_bot_print = "Bot 2"
        dfn_bot_print = "Bot 1"
    Poo_Cannon = PooCannon(atk_bot_str, dfn_bot_agl)
    Vomit_Cloud = VomitCloud(atk_bot_str, dfn_bot_spd)
    Diarrhea_Hurricane = DiarrheaHurricane(atk_bot_spd, dfn_bot_spd)
    current_attack = int(input(
        Fore.LIGHTGREEN_EX + atk_bot_print + ", which attack do you want to use? \n Type 1 for Poo Cannon \n Type 2 for Vomit Cloud \n Type 3 for Diarrhea Hurricane \n"))
    if current_attack == 1:
        print(Fore.RED + atk_bot_print + " used POO CANNON!!!")
        value = random.randrange(1, 100)
        if value > Poo_Cannon.dodge:
            print(Fore.LIGHTYELLOW_EX + dfn_bot_print + " couldn't dodge the poo and GOT HIT!")
            dfn_bot_health = dfn_bot_health - Poo_Cannon.damage
            print(atk_bot_print + " Health:" + str(round(atk_bot_health)))
            print(dfn_bot_print + " Health:" + str(round(dfn_bot_health)))
            if atk_bot == BotOne:
                bot2health = dfn_bot_health
            else:
                bot1health = dfn_bot_health

            if dfn_bot_health <= 0:
                print(Fore.YELLOW + atk_bot_print + " WON!!!")
                return quit()
        else:
            return print(dfn_bot_print + " dodged the POO CANNON!!!")
    if current_attack == 2:
        print(Fore.RED + atk_bot_print + " used VOMIT CLOUD!!!")
        value = random.randrange(1, 100)
        if value > Vomit_Cloud.dodge:
            print(Fore.LIGHTYELLOW_EX + dfn_bot_print + " couldn't run away from the VOMIT CLOUD and breathed it all in!!!")
            dfn_bot_health = dfn_bot_health - Vomit_Cloud.damage
            print(atk_bot_print + " Health:" + str(round(atk_bot_health)))
            print(dfn_bot_print + " Health:" + str(round(dfn_bot_health)))
            if atk_bot == BotOne:
                bot2health = dfn_bot_health
            else:
                bot1health = dfn_bot_health

            if dfn_bot_health <= 0:
                print(Fore.YELLOW + atk_bot_print + " WON!!!")
                return quit()
        else:
            return print(dfn_bot_print + " outran the VOMIT CLOUD!!!")
    if current_attack == 3:
        print(Fore.RED + atk_bot_print + " used DIARRHEA HURRICANE!!!")
        value = random.randrange(1, 100)
        if value > Diarrhea_Hurricane.dodge:
            print(Fore.LIGHTYELLOW_EX + dfn_bot_print + " couldn't run away and got stuck in the DIARRHEA HURRICANE!!!")
            dfn_bot_health = dfn_bot_health - Diarrhea_Hurricane.damage
            print(atk_bot_print + " Health:" + str(round(atk_bot_health)))
            print(dfn_bot_print + " Health:" + str(round(dfn_bot_health)))
            if atk_bot == BotOne:
                bot2health = dfn_bot_health
            else:
                bot1health = dfn_bot_health

            if dfn_bot_health <= 0:
                print(Fore.YELLOW + atk_bot_print + " WON!!!")
                return quit()
        else:
            return print(dfn_bot_print + " ran away from the DIARRHEA HURRICANE!!!")



while 2 + 2 == 4:
    attack(BotOne, BotOne.strength, BotOne.speed, BotTwo.agility, BotTwo.speed, bot2health, bot1health)
    attack(BotTwo, BotTwo.strength, BotTwo.speed, BotOne.agility, BotOne.speed, bot1health, bot2health)