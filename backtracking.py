import json
import sys
import pandas as pd
from datetime import datetime
from datetime import date



def d_bt(stop_points):
    begin_stop_point = datetime.timestamp(datetime.strptime(stop_points['properties']['start_time'], '%Y-%m-%dT%H:%M:%S'))
    end_stop_point = datetime.timestamp(datetime.strptime(stop_points['properties']['end_time'], '%Y-%m-%dT%H:%M:%S'))

    backtracking_threshold = 0.4 #min percentage at which a point will be labeled as backtracking
    backtracking_timer  = 30 #interval used to gather gps points before and after the stop point

    print(stop_points['properties']['start_time'])
    print('\n')

    with open('data/output.json', 'r+') as infile:
        file_data = json.load(infile)
        points_before_stop = [] #array consisting of all points that fall under the interval before the stop point
        points_after_stop = [] #array consisting of all points that fall under the interval after the stop point

        for features in file_data['gps']:
            diff_b = begin_stop_point - features['timestamp']//1000
            diff_e = end_stop_point - features['timestamp']//1000
            
            if(0 < diff_b < backtracking_timer):
                points_before_stop.append(features) #if stop point falls under invertal before stop point add it to correct the array
            
            if(-backtracking_timer < diff_e < 0):
                points_after_stop.append(features) #if stop point falls under invertal after stop point add it to correct the array
                
        points_after_stop.reverse() #reverse the array so all pairs are correct
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
            
            print(diff)
            heading_diff = 165 < abs(diff) < 195  #check if heading difference between 2 points falls between given parameters
            if heading_diff == True:
                true_head = true_head + 1
            else:
                false_head = false_head + 1

        #print(true_head, false_head)
        if min(lpbs, lpas) > 0:
            backtracking_probability = true_head/min(lpbs, lpas) #calculcate the percentage of pairs that are marked as backtracking
        else:
            backtracking_probability = 0.00000001 # 0.000000001 is used to be able to distinguish between a point that just has 0% backtracking or a point where backtracking is just not possible
            
        backtracking_bool = False

        if backtracking_probability >= backtracking_threshold: #if backtracking probability is higher than the threshold mark it as such
            backtracking_bool = True
        
        if backtracking_probability == 0.00000001:
            return backtracking_bool, 'Backtracking not possible' #distinguish between a point that doesn't backtrack or a point that can't possibly be a backtracking point, example: starting point can't be a backtracking point
        else:
            return backtracking_bool, backtracking_probability # return value is a tuple
        
        

with open('data/result.json') as file:
    file_data = json.load(file)

    for features in file_data['features']:
        d_bt(features)