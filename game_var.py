import game_sql

player_name = ""

game_airports = {}

boxes_to_transport = 15

home_airport = "EFHK"

airplane = 1

boxes_delivered = 0 

boxes_in_plane = 0

plane_cap = game_sql.airplane_info(airplane)[3]