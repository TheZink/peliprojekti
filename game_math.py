# This file contains all the functions needed to do math ingame

from geopy.distance import geodesic

# This function calculates the distance between any 2 airport locations given
# distance return in km
def distance_calculate(latitude1, longitude1, latitude2, longitude2):
    location1 = (latitude1, longitude1)
    location2 = (latitude2, longitude2)

    distance = geodesic(location1, location2).km

    # return distance in kilometers
    return distance


# This function calculates how much fuel airplane has used
# fuel_burn_rate is in database in airplane table
def calculate_fuel(distance, fuel_burn_rate):
    # fuel_burn_rate in database in litres per 100km per passenger
    # calculate litres used
    fuel_consumed = distance * (fuel_burn_rate / 100)
    # return used fuel in litres
    return fuel_consumed


# Function to calculate time spent while flying
# distance is in km
# speed in database is in metres per second
def calculate_time_spent(distance, speed):
    time_spent = distance / (speed * 3.6)
    # return time_spend in hours
    return time_spent


# Function to calculate score for player
# def calculate_score(flight_time, fuel_used, money ):
    

