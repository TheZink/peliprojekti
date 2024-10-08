# This file runs all the functions at the end of the game

import game_sql, game_var

def gameover():
    
# print congratulations to player

    print("Onnea! Olet läpäissyt pelin!")
    print ("Haluatko pelata uusiksi?")
    print()

# print statistics
    print()
    #print(f"Pisteet: {game_sql.close_game(game_var.player_name)[4]}")
    print(f"Käytetty lentoaika: {game_sql.close_game(game_var.player_name)[1]} tuntia.")
    print(f"Lennetty matka yhteensä: {game_sql.close_game(game_var.player_name)[0]} kilometriä")
    print(f"Kulutettu polttoaine: {game_sql.close_game(game_var.player_name)[2]} litraa.")
    print()
    

# ask player to play again or quit

    print("Haluatko jatkaa vai lopettaa?")
    print("R aloittaa uusiksi, Q lopettaa.")
    print()

    while True:
        # user input
        answer = str.upper(input("Syötä vaihtoehtosi: "))
        if answer == "R":
            print ("Alustetaan peli uudestaan")
            return True
            
        elif answer == "Q":
            # go back to main and return false boolean
            return False 
        else:
            print ("Väärä valinta. Valitse 'R' jotta jatkuu 'Q' lopetat pelin.")   

# at the end return back to main.py with return

#while gameover = True
    #gamedisplay = "game over, press ok to play again or Q to quit"
   
