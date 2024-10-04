# This file contains all the functions needed to do math ingame

import game_sql
from geopy.distance import geodesic


# This function calculates the distance between any 2 airport locations given
def distance_calculate(latitude1, longitude1, latitude2, longitude2):
    location1 = (latitude1, longitude1)
    location2 = (latitude2, longitude2)

    distance = geodesic(location1, location2).kilometers

    return distance


# This function calculates how much fuel airplane has used
def calculate_fuel(distance, fuel_burn_rate):
    fuel_consumed = distance * fuel_burn_rate
    # fuel burn rate is in database in airplane table
    return fuel_consumed


# time spent:
def calculate_time_spent(distance, speed):
    time_spent = distance / speed
    return time_spent


# score:
# def calculate_score(flight_time, fuel_used, money ):
    

