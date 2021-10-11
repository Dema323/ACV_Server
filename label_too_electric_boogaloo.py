import json
from geopy import distance
from backtracking import backtrackingcompare

def electric_boogaloo(filename='data/result.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        for i in range(0, len(file_data['features'])):
            features = file_data['features']
            if(backtrackingcompare(features[i]) == True):
                if(features[i-1]['type'] == 2):
                    features[i]['type'] = 3
                else:
                    features[i]['type'] = 4
                print(features[i])
        file.seek(0)
        json.dump(file_data, file, indent=4)


electric_boogaloo()
