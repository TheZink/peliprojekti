# This file contains all functions to and from our database

import mysql.connector, game_var, random

game_airports = {}


yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="rahtipeli",
    user="pilotti",
    password="pilotti12345",
    autocommit=True,
    collation='utf8mb4_unicode_ci'
    )


def create_users(player_name: str):
    sql = f"INSERT INTO PLAYER (name,ap_ident,distance,used_time,cons_gas,money,score) VALUES ('{player_name}','{game_var.home_airport}',0,0,0,0,0);"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    user_id = kursori.lastrowid
    game_var.player_id = user_id


# Function select randomly airports from designed continent and add them to dictionary.
# Its also select random values of boxes for each airports.
def create_game(game_airports: dict):
    sql = f"SELECT ident FROM airport WHERE continent = '{game_var.home_continent}'"
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
def get_information(ident: str):
    sql = f"SELECT airport.name, airport.municipality, country.name FROM airport, country WHERE airport.ident = '{ident}' and airport.iso_country = country.iso_country;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    for info in tulos:
        # return ap name, ap municipality, ap country name
        return(info[0],info[1],info[2])


# Function to get coordinates of any given airport identified by ident
def get_coordinates(ident: str):
    sql = f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport WHERE airport.ident = '{ident}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    for kordinaatti in tulos:
        # return latitude, longitude coordinates
        place = kordinaatti[0], kordinaatti[1]
        return place # return coordinates


# Function to get info from airplane name, model, fuel consume, capasity
def airplane_info(plane_id: int):
    sql = f"SELECT airplane.plane_id, airplane.name, airplane.consume, airplane.speed, airplane.capasity FROM airplane WHERE airplane.plane_id = '{plane_id}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    for content in tulos:
        # return: ap name, ap fuel ratio litres per 100km per passenger, ap speed in m/s and ap max box capasity
        return (content[1], content[2], content[3], content[4])


# Function to update player values
def update_game(player_name: str,distance: float,used_time: float,cons_gas: float):
    # distance in km, used_time in hours, cons_gas in litres
    sql = f"UPDATE player SET distance = distance+{distance}, used_time = used_time+{used_time}, cons_gas = cons_gas+{cons_gas} WHERE name = '{player_name}' and player_id = {game_var.player_id};"
    kursori = yhteys.cursor()
    kursori.execute(sql)


# Function to get players info and
# return traveled distance, used time, used fuel, money and score
def close_game(player_name: str):
    sql = f"SELECT * FROM player WHERE name = '{player_name}' and player_id = {game_var.player_id}"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    for player in tulos:
        # return: distance, used_time, cons_gas, money, score
        return(player[3],player[4],player[5],player[6],player[7])
