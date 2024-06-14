import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS hotels (hotel_id text PRIMARY KEY,\
    name text, stars real, rate real, city text)"

create_hotel = "INSERT INTO hotels VALUES ('omega', 'Omega Hotel', 2.1, 190.52, 'Villa Cubas')"

cursor.execute(create_table)
cursor.execute(create_hotel)

connection.commit()
connection.close()