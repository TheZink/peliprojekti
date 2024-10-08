# This file runs programs main structure

# - ----- ----- ----- ----- ----- ----- ----- -----
# - R A H T I P E L I   2 0 2 4
# - Welcome to Rahtipeli! You are an airplane pilot
# - and your task is to transport cargo!
# - People depend on you to do the job and get
# - random stuff for people! Go go go!
# - ----- ----- ----- ----- ----- ----- ----- -----

import game_start, game_go, game_over

# REQUIREMENTS!
# Python runtime enviroment and IDE
# install geopy python library

# Tell the game story
print()
print("-= R A H T I P E L I  2 0 2 4 =-")
print()
print("Tervetuloa pelaamaan rahtipeliä!")
print()
print("---------------------------------------------")
print("Nyt on hätätilanne!")
print("Joulupukin tilaamat lasten joululahjat on toimitettu")
print("Kiinasta tehtailta ihan väärille lentokentille.")
print("Olet yksi vapaaehtoisista lentäjistä lähdössä hakemaan lahjoja.")
print("Tehtäväsi on hakea lahjalaatikoita muilta lentokentiltä")
print("ja toimittaa ne oikeaan paikkaan!")
print("Lentokoneesi on valmiina lentokentällä!")
print("---------------------------------------------")
print()

while True:

    # functions to setup new game for new player
    # in game_start.py
    game_start.set_new_player()
    game_start.set_airports()
    game_start.print_startinfo()

    # functions to run this game session
    # in game_go.py
    game_go.random_5_airports()
    # game_go.py is independent game engine
    # controls game flow independently


    # functions to end this game session
    # in game_over.py
    end_game = game_over.gameover()
    if end_game == False:
        break
