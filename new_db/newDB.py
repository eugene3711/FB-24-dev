import sqlite3

with sqlite3.connect('C:/Users/Евгений/Desktop/FBMap24 Devs/new_db/newDB.db') as connection:
    cursor = connection.cursor()

    try:
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS development (
                id 		INTEGER PRIMARY KEY AUTOINCREMENT,
                name     TEXT NOT NULL UNIQUE,
                dev_id TEXT,                 
                fb_id TEXT,
                fb_name TEXT,
                region TEXT,
                type TEXT,
                latitude REAL,
                longitude REAL      
                );
                '''
        )
    except sqlite3.Error as e:
        print(f"Не удалось создать отношение Tag \n Ошибка базы данных {e}")
    except Exception as e:
        print(f"Не удалось создать отношение Tag \n Ошибка {e}")

    try:
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS targeting (
                id 		INTEGER PRIMARY KEY AUTOINCREMENT,
                fb_id     INTEGER NOT NULL REFERENCES development(fb_id),                
                radius INTEGER,
                latitude REAL,
                longitude REAL
                );
                '''
        )
    except sqlite3.Error as e:
        print(f"Не удалось создать отношение AdTag \n Ошибка базы данных {e}")
    except Exception as e:
        print(f"Не удалось создать отношение AdTag \n Ошибка {e}")
