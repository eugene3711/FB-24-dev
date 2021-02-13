import csv

import time
start_time = time.time()

spend = []
id_list = {}
result = [['name','id','fb_id', 'fb_name', 'type','lat','lon'],]

with open('C:/Users/Евгений/Desktop/Dev Stat upd/FacebookMapDec2020Try/new_db/list/ids.csv', 'r') as f:
    reader = csv.reader(f)

    # read file row by row
    for row in reader:
        try:
            id_list.update({row[0]:row[1]})
        except Exception as e:
            print(e)

with open('C:/Users/Евгений/Desktop/Dev Stat upd/FacebookMapDec2020Try/new_db/list/list.csv', 'r') as f:
    reader = csv.reader(f)

    # read file row by row
    for row in reader:       
        try:
            for name, fb_id in id_list.items():
                found_id = "none"
                dev_name = row[0]
                if ',' in dev_name:
                    dev_name = dev_name[:dev_name.find(',')]
                if dev_name.lower() in name.lower():                    
                    result.append([row[0],row[1],fb_id, name,row[3],row[4],row[5]])  
        except Exception as e:
            print(e)

with open('C:/Users/Евгений/Desktop/Dev Stat upd/FacebookMapDec2020Try/new_db/list/done.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')     
    for line in result:                             
        filewriter.writerow(line)

print("--- %s seconds ---" % (time.time() - start_time))