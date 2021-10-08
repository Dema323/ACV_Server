import json
from geopy import distance
import geopandas

def location_visited_multiple_times(given_coordinate,filename='data/result.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        count = 0
        for i in file_data['features']:
            coordinate = i['geometry']['coordinates']
            points_distance = distance.distance(coordinate, given_coordinate).meters
            if (points_distance < 2):
                count+=1


            if (count >= 2):
                result = True
            else:
                result = False

        # print(result)

# test = [ 4.7265648, 50.8472322 ]
# location_visited_multiple_times(test)
