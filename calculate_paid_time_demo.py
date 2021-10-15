import json
import pandas as pd
from datetime import datetime
from datetime import date


def calculate_paid_time(filename='data/removed.json'):
    start_points = []
    end_points = []
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        for features in file_data['features']:

            if features['type'] == 1:
                # type 1 is a restaurant that gets added to a start_points array
                start_points.append(pd.to_datetime(features['properties']['end_time'], format='%Y-%m-%d'))

                # type 2 is a delivery place that gets added to stop_points array
            if features['type'] == 2:
                end_points.append(pd.to_datetime(features['properties']['start_time'], format='%Y-%m-%d'))

    total_paid_time = 0
    #there will always be an equal amount of start and stop points OR more start points then end points (Can't end what you didn't start)
    #So iterating over end points will guarantee an equal amount of start and stop points
    for i in range(len(end_points)):
        #measure amount of time between start and end point
        diff = end_points[i] - start_points[i]      
        total_paid_time = total_paid_time + diff.seconds
    print("total:"+str(total_paid_time))
    
    # write total paid time to file
    with open('data/paid_time.json', 'w') as outfile:
        #json.dump(data, outfile)
        outfile.write(str(total_paid_time) + '\n')
calculate_paid_time()