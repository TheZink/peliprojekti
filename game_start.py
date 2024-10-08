# This files runs new game setup for new player

import game_sql, game_var

#game_airports = {}
#boxes_to_transport = 15
#home_airport = "EFHK"
#airplane = 1
# Following game progress in game_go
#boxes_delivered = 0 
#boxes_in_plane = 0
#plane_cap = game_sql.airplane_info(airplane)[3]

# Setup new player info
def set_new_player():
    game_var.player_name = input("Kirjoita nimesi tähän: ")
    game_sql.create_users(game_var.player_name)
    print(f"Tervetuloa pilotti {game_var.player_name}")
    print()

# Setup airports and boxes for this game session
def set_airports():
    game_sql.create_game(game_var.game_airports)

# print the start info to player
def print_startinfo():
    print(f"Olet tällä hetkellä {game_sql.get_information(game_var.home_airport)[0]} lentokentällä\nSe sijaitsee maassa {game_sql.get_information(game_var.home_airport)[2]}.")
    print(f"Tämä kenttä on kotikenttäsi, josta lähdet liikkeelle\nja jonne sinun tulee noutaa laatikoita.")
    print()

    # kerrotaan pelaajalle hänen lentokoneen tiedot
    print(f"Käytössäsi on hieno {game_sql.airplane_info(game_var.airplane)[0]} lentokone,\njoka kuluttaa {game_sql.airplane_info(game_var.airplane)[1]} litraa bensaa per 100km\nja joka lentää {(game_sql.airplane_info(game_var.airplane)[2])*3.6:.0f} km/h nopeudella\nja johon mahtuu {game_sql.airplane_info(game_var.airplane)[3]} laatikkoa kyytiin.\nKone on tällä hetkellä tyhjä.")
    print()



# after this we continue in game_go.py as player plays the game
