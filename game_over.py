# This file runs all the functions at the end of the game

import game_sql, game_start, game_math

def gameover(player_name):
    
# print congratulations to player

    print("congrats on completing the game!")
    print ("would you like to play again?")

# print statistics

    print(f"score: {game_sql.close_game(player_name)[4]}")
    print(f"Time played: {game_sql.close_game(player_name)[1]} minutes")
    print(f"Consumed fuel: {game_sql.close_game(player_name)[2]}")
    

# ask player to play again or quit

    print("do you want to play again or quit?")
    print("Press R to restart or Q to quit.")

    while True:
        # user input
        answer = input ("user answer: ")
        if answer == "R":
            print ("Retart the game")
        elif answer == "Q":
            print("Quit the game, Thanks for playing!")
            break  
        else:
            print ("Invalid input. Please press 'R' to continue or 'Q' to quit the game")   

# at the end

#while gameover = True
    #gamedisplay = "game over, press ok to play again or Q to quit"


gameover("Ilkka")

   
