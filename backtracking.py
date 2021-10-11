import json
import sys
import pandas as pd
from datetime import datetime
from datetime import date



def d_bt(stop_points):
    begin_stop_point = datetime.timestamp(datetime.strptime(stop_points['properties']['start_time'], '%Y-%m-%dT%H:%M:%S'))
    end_stop_point = datetime.timestamp(datetime.strptime(stop_points['properties']['end_time'], '%Y-%m-%dT%H:%M:%S'))


    with open('data/output.json', 'r+') as infile:
        file_data = json.load(infile)
        points_before_stop = []
        points_after_stop = []

        for features in file_data['gps']:
            diff_b = begin_stop_point - features['timestamp']//1000
            diff_e = end_stop_point - features['timestamp']//1000
            
            if(0 < diff_b < 15):
                points_before_stop.append(features)
            
            if(-15 < diff_e < 0):
                points_after_stop.append(features)
                
        points_after_stop.reverse()
        lpbs = len(points_before_stop)
        lpas = len(points_after_stop)

        print(lpbs, lpas)
        #print(min(lpbs, lpas))
        #print('\n')
        i = 0
        true_head = 0
        false_head = 0
        for i in range(min(lpbs, lpas)):
            diff = points_before_stop[i]['coords']['heading'] - points_after_stop[i]['coords']['heading']

            heading_diff = 170 < abs(diff) < 190
            if heading_diff == True:
                true_head = true_head + 1
            else:
                false_head = false_head + 1

        #print(true_head, false_head)
        if min(lpbs, lpas) > 0:
            backtracking_probability = true_head/min(lpbs, lpas)
        else:
            backtracking_probability = 0
            
        backtracking_bool = False

        if(backtracking_probability > 0.5):
            backtracking_bool = True
        
        return backtracking_bool, backtracking_probability
        
        # return value is a tuple

with open('data/result.json') as file:
    file_data = json.load(file)

    for features in file_data['features']:
        d_bt(features)