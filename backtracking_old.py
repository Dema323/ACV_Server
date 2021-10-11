import json
import sys
import pandas as pd
from datetime import datetime
from datetime import date

#def backtracking(filename='data/result.json'):
#    with open(filename, 'r+') as file:
#        file_data = json.load(file)
#        
#        
#        for features in file_data['features']:
#            
#            
#            #backtrackingcompare(startx,endx)
#            y = backtrackingcompare(features)
            
        
        
        
#        startx = datetime.timestamp(datetime.strptime(file_data['properties']['start_time'], '%Y-%m-%dT%H:%M:%S'))
            
#        endx = datetime.timestamp(datetime.strptime(file_data['properties']['end_time'], '%Y-%m-%dT%H:%M:%S'))
           
#        bbb = backtrackingcompare(startx,endx)
#        print(bbb)
#    return bbb
        
        
        
        
        
        
    
                
    
        
        
        
        
def backtrackingcompare(x,filename='data/output.json'):
    startx = datetime.timestamp(datetime.strptime(x['properties']['start_time'], '%Y-%m-%dT%H:%M:%S'))
    endx = datetime.timestamp(datetime.strptime(x['properties']['end_time'], '%Y-%m-%dT%H:%M:%S'))
    headx = 100000
    heady = 100000
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        for features in file_data['gps']:
            
            
            if features['timestamp']//1000 == startx:
                
                headx = features['coords']['heading']
            if features['timestamp']//1000 == endx:
                
                heady = features['coords']['heading']
            
            
    
            
            
    diff = headx - heady
    
    bool = 170 < abs(diff) <190
    
    
    return bool




