import json
from geopy import distance
import backtracking
import location_visited_multiple_times



# def add_label(filename='data/result.json'):
#     with open(filename, 'r+') as file:
#         file_data = json.load(file)
#         for i in range(0, len(file_data['features'])):
#             features = file_data['features']
#             coordinate = features[i]['geometry']['coordinates']
#             print(coordinate)
#             if(not location_visited_multiple_times.location_visited_multiple_times(coordinate)):
#                 if(backtracking.backtrackingcompare(features[i])):
#                     features[i]['type'] = 3
#                 #     if(point_already_restaurant == False):
#                 #         features[i]['type']=1
#                 #         point_already_restaurant = True
#                 #     else:
#                 #         features[i]['type']=2
#                 #         point_already_restaurant = False
#                 # else:
#                 #     if(point_already_restaurant == False):
#                 #         features[i]['type']=3
#                 #         point_already_restaurant = True
#                 #     else:
#                 #         features[i]['type']=4
#                 #         point_already_restaurant = False
#             else:
#                 features[i]['type']=5


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
