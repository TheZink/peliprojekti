# This file runs all the functions at the end of the game

import game_sql, game_var

def gameover():
    
# print congratulations to player

    print("congrats on completing the game!")
    print ("Haluatko pelata uusiksi?")

# print statistics

    print(f"Pisteet: {game_sql.close_game(game_var.player_name)[4]}")
    print(f"Pelattu aika: {game_sql.close_game(game_var.player_name)[1]} min")
    print(f"Kulutettu polttoaine: {game_sql.close_game(game_var.player_name)[2]}")
    

# ask player to play again or quit

    print("Haluatko jatkaa vai lopettaa?")
    print("R aloittaa uusiksi, Q lopettaa.")

    while True:
        # user input
        answer = input ("Syötä vaihtoehtosi: ")
        if answer == "R":
            print ("Alustetaan peli uudestaan")
            return True
            
        elif answer == "Q":
            return False 
        else:
            print ("Väärä valinta. Valitse 'R' jotta jatkuu 'Q' lopetat pelin.")   

# at the end return back to main.py with return

#while gameover = True
    #gamedisplay = "game over, press ok to play again or Q to quit"
   
