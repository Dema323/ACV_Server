import json
from geopy import distance
import geopandas
from datetime import datetime
from datetime import date

def acceleration(interval_time,filename='data/result.json', filename2 ='data/output.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        for i in file_data['features']:
            end_time = datetime.timestamp(datetime.strptime(i['properties']['end_time'], '%Y-%m-%dT%H:%M:%S'))

    with open(filename2, 'r+') as file:
        for i in filename2['gps']:
            timestamp = int(str(i['timestamp'])[:-3])
            print(timestamp)


acceleration(0)
