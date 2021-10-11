import json
import backtracking
import average_speed as avg_s

with open('data/result.json', 'r+') as file:

    file_data = json.load(file)
    for features in file_data['features']:
        start = features['properties']['start_time']
        end = features['properties']['end_time']
        features['properties']['avgspeed'] = avg_s.calculate_avg_speed(start,end)
        features['properties']['backtracking'] = backtracking.d_bt(features)[0]
        features['properties']['backtracking_probability'] = backtracking.d_bt(features)[1]
        
    file.seek(0)
    json.dump(file_data, file, indent=4)