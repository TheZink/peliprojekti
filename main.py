# This file runs programs main structure

# - ----- ----- ----- ----- ----- ----- ----- -----
# - R A H T I P E L I   2 0 2 4
# - Welcome to Rahtipeli! You are an airplane pilot
# - and your task is to transport cargo!
# - People depend on you to do the job and get
# - random stuff for people! Go go go!
# - ----- ----- ----- ----- ----- ----- ----- -----

import game_start, game_go, game_over, game_var

# REQUIREMENTS!
# Python runtime enviroment and IDE
# install sql-connector-python
# install pysql
# install geopy python library

'''
Jos halutaan värikästä tekstiä terminaaliin:
'''
'''
from termcolor import colored
print(colored('hello', 'red'), colored('world', 'green'))
'''
'''
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
'''
from colorama import Fore


# Tell the game story
print()
print()
print(Fore.GREEN + "---------------------------------------------")
print()
print()
print(Fore.RED + "-======= R A H T I P E L I  2 0 2 4 =======-")
print()
print()
print(Fore.RED + "Tervetuloa pelaamaan rahtipeliä!")
print(Fore.RESET)
print()
print("Nyt on hätätilanne!")
print("Joulupukin tilaamat lasten joululahjat on toimitettu")
print("Kiinasta tehtailta ihan väärille lentokentille.")
print("Olet yksi vapaaehtoisista lentäjistä lähdössä hakemaan lahjoja.")
print("Tehtäväsi on hakea lahjalaatikoita muilta lentokentiltä")
print("ja toimittaa ne oikeaan paikkaan!")
print("Lentokoneesi on valmiina lentokentällä!")
print()
print(Fore.GREEN + "---------------------------------------------")
print(Fore.RESET)

while True:

    # functions to setup new game for new player
    # in game_start.py
    game_start.set_new_player()
    game_start.set_airports()
    game_start.print_startinfo()

    # functions to run this game session
    # in game_go.py and start game from home
    game_go.random_5_airports(game_var.home_airport)
    # game_go.py is independent game engine
    # controls game flow independently


    # functions to end this game session
    # in game_over.py
    end_game = game_over.gameover()
    if end_game == False:
        break
