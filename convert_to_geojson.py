import json
from datetime import datetime
import glob
import os

list_of_files = glob.glob('../temp/*json') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getmtime) # get newest json file in folder


#This file only serves to change a json into a geojson
#There is no logic here, Its only job is to format the data

with open(latest_file,"r") as infile, open('data/output.json',"w") as outfile:
    outfile.write('{ "gps" : ')
    for line in infile:
        line = line.replace("\\", "")
        line = line.replace('"[', "[")
        line = line.replace(']"', "]")
        outfile.write(line)
    outfile.write("}")

f = open('data/output.json',)
data = json.load(f)


points_list = []

for point in data['gps']:
    timestamp = point['timestamp']

    latitude = point['coords']['latitude']
 
    longitude = point['coords']['longitude']

    speed = point['coords']['speed']

    point_list = [timestamp, latitude, longitude, speed]
    points_list.append(point_list)



with open('data/output.geojson',"w") as outfile:
    outfile.write('{' + '\n' + '"type": "FeatureCollection",' + '\n'
    + '"name": "testdata_geolife2",' + '\n'
    + '"crs": { "type": "output", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },' + '\n'
    + '"features": [' + '\n')
    points = 1
    i = 1
    for x in points_list:
        c_timestamp = int(str(x[0])[:-3])
        dt_object = datetime.fromtimestamp(c_timestamp)
        ##print(len(points_list), i)
        if len(points_list) == i:
            outfile.write('{ "type": "Feature", "properties": { "id": '+ str(i) + ', "sequence": ' + str(i) + ', "trajectory_id": 1, "tracker": 19, "t": "'+ str(dt_object) + '+00" }, "geometry": { "type": "Point", "coordinates": [ ' + str(x[2]) + ', '+ str(x[1]) + ' ] } }' + '\n')
        else:
            outfile.write('{ "type": "Feature", "properties": { "id": '+ str(i) + ', "sequence": ' + str(i) + ', "trajectory_id": 1, "tracker": 19, "t": "'+ str(dt_object) + '+00" }, "geometry": { "type": "Point", "coordinates": [ ' + str(x[2]) + ', '+ str(x[1]) + ' ] } },' + '\n')
        i= i+1
    outfile.write(']' + '\n'
        + '}' + '\n')
