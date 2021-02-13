def get_geo():
    with sqlite3.connect('C:/Users/Евгений/Desktop/Dev Stat upd/FacebookMapDec2020Try/previous/database.db') as con:
        try:
            cur = con.execute(
                'SELECT campaigns.campaign_name, '
                '       targeting.distance_unit,'
                '       targeting.latitude,'
                '       targeting.longitude,'
                '       targeting.radius     '
                'FROM campaigns JOIN targeting ON campaigns.id=targeting.targeting_id '
            )
            rows = cur.fetchall()
            print(type(rows))
        except sqlite3.IntegrityError as e:
            print(e)
            return f"{e}", 409
        except Exception as e:
            print(e)
            return f"{e}", 409

    '''
    map_dict = {}
    for row in rows:
        map_dict[f'{row[0]}'] = {
            'distance_unit': row[1],
            'latitude': row[2],
            'longitude': row[3],
            'radius': row[4]
        }
    
    geo_data = []
    for row in rows:
        geo_data.append(
            {'campaign_name': row[0],
             'distance_unit': row[1],
             'latitude':      row[2],
             'longitude':     row[3],
             'radius':        row[4]
            }
        )
'''
    geo_data = []
    for row in rows:
        geo_data.append(
            {'name': row[0],
             'distance_unit': row[1],
             'id': 'random',
             'geo': [{
             'latitude':      row[2],
             'longitude':     row[3],
             'radius':        row[4]
             }]
            }
        )


db_imitation = {
    "developments": [
        {"name": "London", "id": 123, "geo": [{"radius": 25, "lat": 51.50, "lon": -0.14}]},
        {"name": "Birmingham", "id": 124, "geo": [{"radius": 15, "lat": 52.37, "lon": -2.19}, 
                                                {"radius": 15, "lat": 52.77, "lon": -1.64}]},
        {"name": "Liverchester", "id": 125, "geo": [{"radius": 10, "lat": 53.77, "lon": -2.71}, 
                                                {"radius": 10, "lat": 53.39, "lon": -2.99},             
                                                {"radius": 10, "lat": 53.48, "lon": -2.24}            
                                                ]}
        ]
}



    print(geo_data)
    print(json.dumps(geo_data))


    return (json.dumps(geo_data))