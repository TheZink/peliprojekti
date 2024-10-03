import game_sql

game_airports = {}

def player_info():
    print("Tervetuloa pelaamaan rahtipeliä! Kerrotko kuka olet?")
    player_name = input("Kirjoita nimesi tähän: ")
    game_sql.create_users(player_name)
    print(f"Tervetuloa {player_name}")

def set_area():
    game_sql.create_game(game_airports)
    
