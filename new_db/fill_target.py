import sqlite3
import requests
import time


def getTargeting(fid):
    token = 'EAAEh8tnwjMcBAJzcMCkmsx1mOxBlW3mPDAy17t86Vvh2NtRJpHRAZAvCFAVsifWyyRKlvcWYFyi13g6l5fHMuzIeQKk8tou9H22PvlHn0nXR4M3ZBC6FfnjkzF6kOxz16svUQoOsLk53dzXNvNEIxEeDRhb70ELYibhjoXswZDZD'
    account = '131341384041787'
    print(fid)
    url = 'https://graph.facebook.com/v7.0/'+fid+'/?fields=id,name,adsets{status,targeting}&access_token='+token

    json_data = requests.get(url).json()
    
    targeting = json_data['adsets']['data']
    locations = "none"
    for adset in targeting:
        if adset['status'] == 'ACTIVE':
            try:
                locations = adset['targeting']['geo_locations']
                break
            except:
                pass
    return locations     

developments = []
with sqlite3.connect('C:/Users/Евгений/Desktop/FBMap24 Devs/new_db/newDB.db') as con:
        try:
            cur = con.execute('''
                SELECT name, fb_id

                FROM development
                '''
            )
            rows = cur.fetchall()
            developments = rows            
        except sqlite3.IntegrityError as e:
            print(e)            
        except Exception as e:
            print(e)

print("Info get")
time.sleep(2)
#developments = developments[1:]

with sqlite3.connect('C:/Users/Евгений/Desktop/FBMap24 Devs/new_db/newDB.db') as con:
    print("New connection")
    for index, dev in enumerate(developments):
        print(f"{index}, {dev}")
        #if index >= 42:

        name, fb_id = dev[0], dev[1]
        print(f"{name}, {fb_id}")
        current_locations = getTargeting(fb_id)

        postcodes = 0
        try:
            postcodes = str(current_locations['zips'])
        except:
            print("No postcodes")

        try:
            check = current_locations['custom_locations']
        except:
            print(f"No locations in {index}, {name}")
            continue

        for loc in current_locations['custom_locations']:
            if loc['distance_unit'] == 'mile':
                radius = int(round(loc['radius']*1.60934))
            else:
                radius = int(loc['radius'])
            try:
                cur = con.execute('''
                    INSERT INTO targeting (fb_id, postcodes, radius, latitude, longitude)
                    VALUES (?, ?, ?, ?, ?)
                    ''',

                    (fb_id,
                    postcodes,
                    radius,
                    loc['latitude'],
                    loc['longitude']
                   ),

                        )
                con.commit()
            except sqlite3.IntegrityError as e:
                print(f"Integrity{e}")

            except Exception as e:
                print(f"General exception{e}")

        try:
            con.commit()
        except sqlite3.IntegrityError as e:
                print(e)
        except Exception as e:
                print(e)
        print(f"Success {index} of {len(developments)}: {name}")
        time.sleep(2)
