import urllib, json
import sqlite3
import random
from random import randint

def getFullTargeting(fb_id):
    with sqlite3.connect('C:/Users/Евгений/Desktop/FBMap24 Devs/new_db/newDB.db') as con:
        try:
            cur = con.execute('''
                    SELECT development.name,
                           development.fb_id,
                           development.region,
                           targeting.radius,                             
                           targeting.latitude,
                           targeting.longitude                            
                                
                    FROM development JOIN targeting ON development.fb_id=targeting.fb_id
                    WHERE development.fb_id=?                    
                    ''',
                    (fb_id,)
                                )
            rows = cur.fetchall()
            #print(rows)
        except sqlite3.IntegrityError as e:
            print(e)
            return f"{e}", 409
        except Exception as e:
            print(e)
            return f"{e}", 409

    geo_data = {'name': rows[0][0], 'id': rows[0][1], 'geo': []}


    for row in rows:
        geo_data['geo'].append(
            {'lat': row[4],
             'lon': row[5],
             'radius': row[3]
                }         
        )
    response = geo_data
    return response

def getTargeting():
    with sqlite3.connect('C:/Users/Евгений/Desktop/FBMap24 Devs/new_db/newDB.db') as con:
        try:
            cur = con.execute('''
                    SELECT development.name,
                           development.fb_id,
                           development.latitude,
                           development.longitude  
                    FROM development 
                    '''
                                )
            rows = cur.fetchall()
            print(type(rows))
        except sqlite3.IntegrityError as e:
            print(e)
            return f"{e}", 409
        except Exception as e:
            print(e)
            return f"{e}", 409

    geo_data = []

    for row in rows:
        geo_data.append(
            {'name': row[0],
             'id': row[1],
             'lat': row[2],
             'lon': row[3]
                }
        )
    response = {"developments": geo_data}
    return response
