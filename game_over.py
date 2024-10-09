# This file runs all the functions at the end of the game

import game_sql, game_var

def gameover():
    # print congratulations to player
    print("Onnea! Olet läpäissyt pelin!")
    print()

    # print statistics
    # print(f"Pisteet: {game_sql.close_game(game_var.player_name)[4]}")
    # print Money...
    print(f"Käytetty lentoaika: {game_sql.close_game(game_var.player_name)[1]:.0f} tuntia.")
    print(f"Lennetty matka yhteensä: {game_sql.close_game(game_var.player_name)[0]:.0f} kilometriä")
    print(f"Kulutettu polttoaine: {game_sql.close_game(game_var.player_name)[2]:.2f} litraa.")
    print()

    # print game high scores
    print("Tähän vielä tuloste pelin Highscore, parhaat 5 pelaajaa?")
    print("1. Mut vielä silti parempi pelaaja")
    print("2. Ihan paras pelaaja")
    print("3. Tosi hyvä pelaaja")
    print("4. Suht hyvä pelaaja")
    print("5. Ihan ok pelaaja")
    print()

    # reset game engine stats
    game_var.boxes_delivered = 0

    # ask player to play again or quit
    print("Haluatko pelata uudestaan vai lopettaa?")
    print("R aloittaa uusiksi, Q lopettaa.")
    print()

    while True:
        # user input
        answer = str.upper(input("Syötä vaihtoehtosi: "))
        print()
        if answer == "R":
            print("Hienoa! Alustetaan peli uudestaan!")
            print()
            # go back to main and return true boolean
            # and game will restart again from beginning
            return True
            
        elif answer == "Q":
            print("Kiitos pelaamisesta! Toivottavasti sinulla oli hauskaa!")
            print()
            # go back to main and return false boolean
            # and game will end
            return False 
        else:
            print("Väärä valinta. Valitse 'R' jotta jatkuu 'Q' lopetat pelin.")
            print()

# at the end return back to main.py with return
