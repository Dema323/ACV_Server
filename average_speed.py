import json
import pandas as pd
from datetime import datetime

def calculate_avg_speed(start_time, end_time):
    start_time = start_time.replace('T', ' ')
    end_time = end_time.replace('T', ' ')
    with open('data/output.json', 'r+') as gpsfile:
        gps_p_file = json.load(gpsfile)
        point_speeds = []

        for point in gps_p_file['gps']:
            timestamp = point['timestamp']

            speed = point['coords']['speed']

            c_timestamp = int(str(timestamp)[:-3])

            dt_object = datetime.fromtimestamp(c_timestamp)
            dt_object = str(dt_object)
            if(dt_object < end_time and dt_object > start_time):
                point_speeds.append(speed)
        
        avg_speed = sum(point_speeds) / len(point_speeds)
        #print(avg_speed)
        return avg_speed
        #print(point_speeds)

            #gps_point_list = [str(dt_object), speed]
            #gps_points_list.append(gps_point_list)
#calculate_avg_speed('2021-10-01T10:51:00', '2021-10-01T10:53:16')