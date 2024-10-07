# This files runs new game setup for new player

import game_sql

game_airports = {}
boxes_to_transport = 15
home_airport = "EFHK"
airplane = 1
player_name = ""
# Following game progress in game_go
boxes_delivered = 0 
boxes_in_plane = 0
plane_cap = game_sql.airplane_info(airplane)[3]

# Setup new player info
def set_new_player():
    print()
    print("-= R A H T I P E L I  2 0 2 4 =-")
    print()
    print("Tervetuloa pelaamaan rahtipeliä!")
    player_name = input("Kirjoita nimesi tähän: ")
    game_sql.create_users(player_name)
    print(f"Tervetuloa pilotti {player_name}")
    print()

# Setup airports and boxes for this game session
def set_airports():
    game_sql.create_game(game_airports)

# Tell the game story
def print_story():
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

# print the start info to player
def print_startinfo():
    print(f"Olet tällä hetkellä {game_sql.get_information(home_airport)[0]} lentokentällä\nSe sijaitsee maassa {game_sql.get_information(home_airport)[2]}.")
    print(f"Tämä kenttä on kotikenttäsi, josta lähdet liikkeelle\nja jonne sinun tulee noutaa laatikoita.")

    # kerrotaan pelaajalle hänen lentokoneen tiedot
    print(f"Käytössäsi on hieno {game_sql.airplane_info(airplane)[0]} lentokone,\njoka kuluttaa {game_sql.airplane_info(airplane)[1]} litraa bensaa per 100km\nja joka lentää {(game_sql.airplane_info(airplane)[2])*3.6:.0f} km/h nopeudella\nja johon mahtuu {game_sql.airplane_info(airplane)[3]} laatikkoa kyytiin.\nKone on tällä hetkellä tyhjä.")


# after this we continue in game_go.py as player plays the game
