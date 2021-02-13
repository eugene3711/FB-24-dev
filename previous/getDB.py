import sqlite3
import requests
import time


def getTargeting():
    token = 'EAAEh8tnwjMcBAJzcMCkmsx1mOxBlW3mPDAy17t86Vvh2NtRJpHRAZAvCFAVsifWyyRKlvcWYFyi13g6l5fHMuzIeQKk8tou9H22PvlHn0nXR4M3ZBC6FfnjkzF6kOxz16svUQoOsLk53dzXNvNEIxEeDRhb70ELYibhjoXswZDZD'
    account = '131341384041787'
    url = f'https://graph.facebook.com/v7.0/act_{account}/adsets?fields=id,name,status,targeting&access_token={token}'

    json_data = requests.get(url).json()

    while json_data['paging']['next']:
        for campaign in json_data['data']:
            id = campaign['id']
            name = campaign['name']
            target = campaign['targeting']['geo_locations']

        print(f"ID: {id}, NAME: {name}")

        with sqlite3.connect('C:/Users/Евгений/PycharmProjects/TestFlask/database.db') as con:
            try:
                cur = con.execute(
                    'INSERT INTO campaigns (campaign_id, campaign_name) '
                    'VALUES (?, ?)',
                    (id, name),
                )
                con.commit()
                targeting_id = cur.lastrowid

            except sqlite3.IntegrityError as e:
                print(e)
                return f"{e}", 409
            except Exception as e:
                print(e)
                return f"{e}", 409

            try:
                for location in target['custom_locations']:

                    cur = con.execute(
                        'INSERT INTO targeting (targeting_id, distance_unit, latitude, longitude, radius) '
                        'VALUES (?, ?, ?, ?, ?)',

                        (targeting_id,
                         location['distance_unit'],
                         location['latitude'],
                         location['longitude'],
                         location['radius']),
                    )
                con.commit()
            except sqlite3.IntegrityError as e:
                print(e)
                return f"{e}", 409
            except Exception as e:
                print(e)
                return f"{e}", 409


        print('Success! Sleeps now')

        time.sleep(30)
        json_data = requests.get(json_data['paging']['next']).json()

getTargeting()

