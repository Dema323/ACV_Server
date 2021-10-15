import json
from geopy import distance
import geopandas

#This measures the distance between all detected stop points
#If there are points that are within x meters from each other
#If a point gets visited more than once it gets marked as "Visited multiple times"
#This part hasn't been implemented/tought through completely yet, so feel free to adapt or change completely

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


