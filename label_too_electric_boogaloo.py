import json
from geopy import distance

def electric_boogaloo(filename='data/result.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        for i in range(0, len(file_data['features'])):
            features = file_data['features']
            if(features[i]['type'] == 3 and features[i-1]['type'] == 1):
                # type 1 bestaat nog niet
                    features[i]['type'] = 2
            else:
                features[i]['type'] = 1


electric_boogaloo()
