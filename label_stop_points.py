import json
from geopy import distance

def add_label(filename='data/result.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        i = 1
        for features in file_data['features']:
            coordinate = features['geometry']['coordinates']
            print(coordinate)
            if(i%2 == 1):
                features['type']= 1
            if(i%2 == 0):
                features['type']= 2
            i = i + 1
        file.seek(0)
        json.dump(file_data, file, indent=4)
    
add_label()