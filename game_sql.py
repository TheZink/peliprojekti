# This file contains all functions to and from our database

import mysql.connector, random
game_airports = {}
yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="rahtipeli",
    user="sinkki",
    password="1234",
    autocommit=True,
    collation='utf8mb4_unicode_ci'
    )

def create_users(player_name):
    sql = f"INSERT INTO PLAYER (name,ap_ident,distance,used_time,cons_gas,money,score) VALUES ('{player_name}','EFHK',0,0,0,0,0);"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    
#Function select randomly airports from EU continents and add them to dictionary. Its also select random values for each airports
def create_game(game_airports):
    sql = f"SELECT ident FROM airport WHERE continent = 'EU'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    for time in range(15):
        choice_airport = random.choice(tulos)
        if choice_airport not in game_airports:
            # add new random airport to dictionary and add random 1-15 boxes to airport
            game_airports[choice_airport[0]] = random.randint(1,15) #Generate random numbers for airport.
    
    return game_airports

# Fuction to get information of any given airport. Fuction return airport details (Name, city and country) 
def get_information(ident):
    sql = f"SELECT airport.name, airport.municipality, country.name FROM airport, country WHERE airport.ident = '{ident}' and airport.iso_country = country.iso_country;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    for info in tulos:
        return(info[0],info[1],info[2])


# Function to get coordinates of any given airport (ident)
def get_coordinates(ident):
    sql = f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport WHERE airport.ident = '{ident}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    for kordinaatti in tulos:
        place = kordinaatti[0], kordinaatti[1]
        return place # return kordinaatit

# function info from airplane name, model, consume, capasity
def airplane_info(plane_id):
    sql = f"SELECT airplane.plane_id, airplane.name, airplane.consume, airplane.speed, airplane.capasity FROM airplane WHERE airplane.plane_id = '{plane_id}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    for content in tulos:
        return (content[1], content[2], content[3], content[4])

        
# function update player values
def update_game(player_name,distance,used_time,cons_gas):
    sql = f"UPDATE player SET distance = distance+{distance}, used_time = used_time+{used_time}, cons_gas = cons_gas+{cons_gas} WHERE name = '{player_name}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)

# Function to get players info. Function return distance, used_time, cons_gas, money and score
def close_game(player_name):
    sql = f"SELECT * FROM player WHERE name = '{player_name}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    
    for player in tulos:
        return(player[3],player[4],player[5],player[6],player[7])
    