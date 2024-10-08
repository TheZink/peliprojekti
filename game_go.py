# This file runs all ingame functions while player plays the game

import game_sql, game_var, game_math, random

# gameplay follow up variables

# airports dictionary has aiport ident and number of boxes in that airport
airports = game_var.game_airports
# home airport ident
location = game_var.home_airport
random_choice, visited, keys = [], [], []

# we give player 5 different airports in random
# Function select randomly 5 airports from game_airports dictionary
# random_choice list gets airport ident codes only from dictionary
def random_5_airports():
    # make list of all keys in games airports
    keys = list(airports.keys())
    # empty random choise list
    random_choice.clear()
    while len(random_choice) < 5:
        # select a random ident from list
        random_ident = random.choice(keys)
        # add random ident to random choise list if not in it and not in visited
        if random_ident not in random_choice:
            if random_ident not in visited:
                if random_ident != game_var.home_airport:
                    random_choice.append(random_ident)
        # repeat until 5 added?
    choose_where_to_go()
    
# print options for player what player can do: choose next airport where to fly
# let player choose using number options? 1 airport1, 2 airport2, 3..., 4..., 5...?
# if lauseella, valitaan pelaajan valitsema kenttä

def choose_where_to_go():
    print("Laatikoita löytyy muun muuassa näistä lentokentiltä:")
    print()
    # print 5 airports (name, distance, boxes)
    number = 1
    for ident in random_choice:
        print(f"{number}. {game_sql.get_information(ident)[0]}, {game_sql.get_information(ident)[2]}, jossa on {airports[ident]} laatikkoa.")
        number += 1
    # make player choose where to go
    choice = int(input("Mille kentälle haluat lentää seuraavaksi?: "))
    print()
    moving_ap2ap(random_choice[choice-1],location)


# transport player from airport to airport
def moving_ap2ap(ident,location):
    # transport player from airport to airport, update location
    prev_coords = game_sql.get_coordinates(location)
    dest_coords = game_sql.get_coordinates(ident)
    location = ident
    if ident != game_var.home_airport:
        visited.append(ident)
    # calculate traveled distance, used time, used fuel
    distance = game_math.distance_calculate(prev_coords[0], prev_coords[1], dest_coords[0], dest_coords[1])
    fuel_burn_rate = game_sql.airplane_info(game_var.airplane)[2]
    speed = game_sql.airplane_info(game_var.airplane)[3]
    fuel_consumed = game_math.calculate_fuel(distance, fuel_burn_rate)
    time_spent = game_math.calculate_time_spent(distance, speed)
    # update database player stats
    # print(f"{game_var.player_name}")
    game_sql.update_game(game_var.player_name, distance, time_spent, fuel_consumed)
    if ident == game_var.home_airport:
        at_home_airport()
    else:
        at_new_airport(location)

def at_new_airport(location):
    empty_room_in_plane = game_sql.airplane_info(game_var.airplane)[3] - game_var.boxes_in_plane
    if airports[location] < empty_room_in_plane:
        loading = airports[location]
    else:
        loading = empty_room_in_plane
    print(f"Saavuit {game_sql.get_information(location)[0]} lentokentälle.\nKentällä on {airports[location]} laatikkoa odottamassa noutoa.\nKoneeseen mahtuu vielä {game_sql.airplane_info(game_var.airplane)[3]-game_var.boxes_in_plane} laatikkoa.")
    print()
    game_var.boxes_in_plane = game_var.boxes_in_plane + loading
    print(f"Koneeseesi lastattiin {loading} laatikkoa.\nKoneessa on nyt {game_var.boxes_in_plane} laatikkoa.")
    print(f"Koneeseen mahtuu vielä {game_sql.airplane_info(game_var.airplane)[3]-game_var.boxes_in_plane} laatikkoa.")
    print()
    if game_var.boxes_in_plane == game_sql.airplane_info(game_var.airplane)[3]:
        print("Nyt olisi hyvä hetki viedä laatikoita kotiin!") # after this direct player to go back home to deliver boxes
        print()
    # give player options what to do next
    player_input = input("Mitä haluat tehdä?\nVoit valita 'jatka' ja hakea lisää laatikoita\ntai viedä jo kyydissä olevat laatikot 'kotiin': ")
    print()
    # player chooses what to do
    if player_input == "jatka": random_5_airports()
    elif player_input == "kotiin": moving_ap2ap(game_var.home_airport,location)



    '''
    if current_boxes > 0:
        boxes_delivered = int(input(f"you have {current_boxes} boxes. How many do you want to deliver?))
        if boxes_delivered > current_boxes:
            print("you can not deliver more boxes than you have.")
        else:
            current_boxes -= boxes_delivered

    '''

def at_home_airport():
    # unload boxes
    # manage and keep track of boxes (picked up into airplane from airport / delivered to airport) 
    game_var.boxes_delivered += game_var.boxes_in_plane
    game_var.boxes_in_plane = 0
    # check if enough boxes at home? if enough go to END GAME
    # repeat until enough boxes delivered
    if game_var.boxes_delivered < game_var.boxes_to_transport:
        print(f"Tervetuloa kotiin!\nKotona on nyt {game_var.boxes_delivered} laatikkoa.\nSinun pitää toimittaa tänne yhteensä {game_var.boxes_to_transport} laatikkoa.\nEli sinun pitää hakea vielä {(game_var.boxes_to_transport)-(game_var.boxes_delivered)} laatikkoa.")
        print(f"Koneesi on taas tyhjä. Eli koneeseen mahtuu taas {game_sql.airplane_info(game_var.airplane)[3]} laatikkoa kyytiin.")
        print()
        random_5_airports()
    # if boxes_delivered >= game_start.boxes_to_transport:
        # end game_go.py and move to game_over.py



'''
Jos halutaan värikästä tekstiä terminaaliin:
from termcolor import colored
print(colored('hello', 'red'), colored('world', 'green'))
'''
