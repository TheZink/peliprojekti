import mysql.connector, random

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

def create_game(game_airports):
    continent = "EU"
    sql = f"SELECT * FROM AIPORT WHERE continent = '{continent}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()


