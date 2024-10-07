# This file runs all ingame functions while player plays the game

import game_sql, game_start, game_math, random

# gameplay follow up variables

# airports dictionary has aiport ident and number of boxes in that airport
airports = game_start.game_airports
location = game_start.home_airport
random_choice, visited = [], []
name = game_start.player_name

# we give player 5 different airports in random

# Function select randomly 5 airports from game_airports dictionary
# random_choice list gets airport ident codes only from dictionary
def random_5_airports():
    random_choice.clear()
    keys = list(airports.keys())
    while len(random_choice) < 5:
        random_ident = random.choice(keys)
        if random_ident not in random_choice and not visited: 
            random_choice.append(random_ident)
    choose_where_to_go()
    
# print options for player what player can do: choose next airport where to fly
# let player choose using number options? 1 airport1, 2 airport2, 3..., 4..., 5...?
# if lauseella, valitaan pelaajan valitsema kenttä

def choose_where_to_go():
    print("Laatikoita löytyy muun muuassa näistä lentokentiltä:")
    # print 5 airports (name, distance, boxes)
    number = 1
    for ident in random_choice:
        print(f"{number}. {game_sql.get_information(ident)[0]}, {game_sql.get_information(ident)[2]}, jossa on {airports[ident]} laatikkoa.")
        number += 1
    # make player choose where to go
    choice = int(input("Mille kentälle haluat lentää seuraavaksi?: "))
    moving_ap2ap(random_choice[choice-1],location)


# transport player from airport to airport
def moving_ap2ap(ident,location):
    # transport player from airport to airport, update location
    prev_coords = game_sql.get_coordinates(location)
    dest_coords = game_sql.get_coordinates(ident)
    location = ident
    visited.append(ident)
    # calculate traveled distance, used time, used fuel
    distance = game_math.distance_calculate(prev_coords[0], prev_coords[1], dest_coords[0], dest_coords[1])
    fuel_burn_rate = game_sql.airplane_info(game_start.airplane)[2]
    speed = game_sql.airplane_info(game_start.airplane)[3]
    fuel_consumed = game_math.calculate_fuel(distance, fuel_burn_rate)
    time_spent = game_math.calculate_time_spent(distance, speed)
    # update database player stats
    game_sql.update_game(name, distance, time_spent, fuel_consumed)
    if ident == game_start.home_airport:
        at_home_airport()
    else:
        at_new_airport(location)

def at_new_airport(location):
    empty_room_in_plane = game_start.plane_cap - game_start.boxes_in_plane
    if airports[location] < empty_room_in_plane:
        loading = airports[location]
    else:
        loading = empty_room_in_plane
    print(f"Saavuit {game_sql.get_information(location)[0]} lentokentälle.\nKentällä on {airports[location]} laatikkoa odottamassa noutoa.\nKoneeseen mahtuu vielä {game_start.plane_cap-game_start.boxes_in_plane} laatikkoa.")
    game_start.boxes_in_plane = game_start.boxes_in_plane + loading
    print(f"Koneeseesi lastattiin {loading} laatikkoa.\nKoneessa on nyt {game_start.boxes_in_plane} laatikkoa.")
    print(f"Koneeseen mahtuu vielä {game_start.plane_cap-game_start.boxes_in_plane} laatikkoa.")
    if game_start.boxes_in_plane == game_start.plane_cap:
        print("Aika viedä laatikot kotiin!") # after this direct player to go back home to deliver boxes
    # give player options what to do next
    player_input = input("Mitä haluat tehdä?\nVoit valita 'jatka' ja hakea lisää laatikoita\ntai viedä jo kyydissä olevat laatikot 'kotiin': ")

    if player_input == "jatka": random_5_airports()
    elif player_input == "kotiin": moving_ap2ap(game_start.home_airport,location)

    # room for boxes in airplane? (airplane capasity, plus if some capasity used at the moment)
    # boxes at current airport? (dictionary of all 15 airports)

    # pickup boxes? (how many available at airport and how many fits in airplane?)
    # print user how much room in plane, how many boxes at airport
    # offer player to choose now many to pickup, can pickup also 0

    #boxes_at_airport = game_sql.airplane_info(airplane)[3]
    #current_boxes = 0
    #picked_up_boxes = 

    '''
    if current_boxes > 0:
        boxes_delivered = int(input(f"you have {current_boxes} boxes. How many do you want to deliver?))
        if boxes_delivered > current_boxes:
            print("you can not deliver more boxes than you have.")
        else:
            current_boxes -= boxes_delivered

    '''
    # choose next airport, home or next 5 random

def at_home_airport():
    print("kotona")
    pass
    # unload boxes
    # check if enough boxes at home? if enough go to END GAME
    # manage and keep track of boxes (picked up into airplane from airport / delivered to airport) 
    # repeat until enough boxes delivered
    # if boxes_delivered >= game_start.boxes_to_transport:
        # end game_go.py and move to game_over.py
    # else: print some stats and choose next 5 random airports


game_start.set_airports()
random_5_airports()
choose_where_to_go()

'''
Jos halutaan värikästä tekstiä terminaaliin:
from termcolor import colored
print(colored('hello', 'red'), colored('world', 'green'))
'''
