import sqlite3
import csv

with open('C:/Users/Евгений/Desktop/FBMap24 Devs/new_db/devs.csv', 'r') as f:
    with sqlite3.connect('C:/Users/Евгений/Desktop/FBMap24 Devs/new_db/newDB.db') as con:
        reader = csv.reader(f)    
        for row in reader:
            try:
                cur = con.execute(
                    'INSERT INTO development (name, dev_id, fb_id, fb_name, region, type, latitude, longitude) '
                    'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                    (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]),
                )
                con.commit()     
            except sqlite3.IntegrityError as e:
                print(e)                
            except Exception as e:
                print(e)