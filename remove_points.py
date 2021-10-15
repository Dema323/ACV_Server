import json


#This code was used to "Save stop points from being deleted"
#The idea was to use a lower time parameter for the movingpandas script which would create more faulty points
#The variables here are arbitrary and should be in balance with the variables chosen for the movingpandas script




def remove_points(filename='data/result.json'):
    dict_data = {}
    correct_data = []
    with open(filename, 'r+') as file:
        file_data = json.load(file)

        for features in file_data['features']:
            if (features['properties']['duration_s'] < 60): #Is the duration of the stop lower then 60s ?
                if (features['properties']['backtracking'] == True): #Is the stoppoint marked as backtracking ?
                    correct_data.append(features) #Yes -> So we save that point
            else:
                correct_data.append(features) #point is above 60s so it also gets saved

    dict_data['type'] = 'FeatureCollection'
    dict_data['features'] = correct_data            
    with open('data/removed.json', 'w') as outfile:
        json.dump(dict_data, outfile, indent=4,separators=(',', ': '))

    

remove_points()
