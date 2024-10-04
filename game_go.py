# This file runs all ingame functions while player plays the game

import game_sql, game_start, game_math, random

# gameplay follow up variables

airports = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10} #game_start.game_airports
boxes_delivered = 0
location = ""
random_choice = []

# print options for player what player can do: choose next airport where to fly
# we give player 5 different airports in random
# let player choose using number options? 1 airport1, 2 airport2, 3..., 4..., 5...?

print(random_choice)
def playthrough():
    while True:
        
        for ident in range(5):
            random_choice.append(random.choice(airports))



    pass

if boxes_delivered >= game_start.boxes_to_transport:
    print("You win!")

print(game_start.testi)

# transport player from airport to airport
# update player info into sql db (distance traveled, time spent, fuel used)
# manage and keep track of boxes (picked up into airplane from airport / delivered to airport) 
# repeat until enough boxes delivered

