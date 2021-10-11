import json
import pandas as pd
from datetime import datetime

def calculate_avg_speed():
    with open('data/result.json', 'r+') as resfile, open('data/output.json', 'r+') as gpsfile:
        stop_points_file = json.load(resfile)
        stop_points = []
        for features in stop_points_file['features']:
            stop_point = []
            #print(features)
            stop_point.append(pd.to_datetime(features['properties']['start_time'], format='%Y-%m-%d'))
            stop_point.append(pd.to_datetime(features['properties']['end_time'], format='%Y-%m-%d'))
            stop_point.append(features['properties']['duration_s'])
            #print(stop_point)
            stop_points.append(stop_point)
        #print(stop_points)

        gps_p_file = json.load(gpsfile)

        gps_points_list = []

        for point in gps_p_file['gps']:
            timestamp = point['timestamp']
            ##print(timestamp)
            latitude = point['coords']['latitude']
            ##print(latitude)
            longitude = point['coords']['longitude']
            ##print(longitude)
            speed = point['coords']['speed']
            ##print(speed)
            c_timestamp = int(str(timestamp)[:-3])
            #print(c_timestamp)
            dt_object = datetime.fromtimestamp(c_timestamp)
            #print(dt_object)
            gps_point_list = [str(dt_object), speed]
            gps_points_list.append(gps_point_list)
        print(gps_points_list)

calculate_avg_speed()