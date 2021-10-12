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
                start_points.append(pd.to_datetime(features['properties']['end_time'], format='%Y-%m-%d'))
                #print("Start")
                #print(start_points)

            if features['type'] == 2:
                end_points.append(pd.to_datetime(features['properties']['start_time'], format='%Y-%m-%d'))
                #print("Stop")
                #print(end_points)
    total_paid_time = 0
    for i in range(len(end_points)):
        diff = end_points[i] - start_points[i]
        #print(diff.seconds)
        total_paid_time = total_paid_time + diff.seconds
    print("total:"+str(total_paid_time))

    #data = {}
    #data['seconds'] = diff.total_seconds()
    
    with open('data/paid_time.json', 'w') as outfile:
        #json.dump(data, outfile)
        outfile.write(str(total_paid_time) + '\n')
calculate_paid_time()