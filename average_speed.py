import json
import pandas as pd
from datetime import datetime

def calculate_avg_speed(start_time, end_time):
    
    #convert timestamp to a datetime by changing T into a space
    start_time = start_time.replace('T', ' ')
    end_time = end_time.replace('T', ' ')


    with open('data/output.json', 'r+') as gpsfile:
        gps_p_file = json.load(gpsfile)
        point_speeds = []

        for point in gps_p_file['gps']:

            timestamp = point['timestamp']
            speed = point['coords']['speed']
            
            #Remove miliseconds from timestamp -> [:-3]
            c_timestamp = int(str(timestamp)[:-3])

            #Turn timestamp into datetime object
            dt_object = datetime.fromtimestamp(c_timestamp)
            dt_object = str(dt_object)

            #This if statement only adds the points that belong to the stop point to the array
            if(dt_object < end_time and dt_object > start_time):
                point_speeds.append(speed)
        
        #Devide sum of all points by the number of points
        avg_speed = sum(point_speeds) / len(point_speeds)

        
        return avg_speed
        

            #gps_point_list = [str(dt_object), speed]
            #gps_points_list.append(gps_point_list)
#calculate_avg_speed('2021-10-01T10:51:00', '2021-10-01T10:53:16')