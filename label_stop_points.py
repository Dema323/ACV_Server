import json

#This script will iterate over all detected stop points and mark them accordingly
#First point gets marked as 1, point following 1 gets marked 2
#Repeat cycle

def add_label(filename='data/removed.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        i = 1
        for features in file_data['features']:
            if(i%2 == 1):
                features['type']= 1
            if(i%2 == 0):
                features['type']= 2
            i = i + 1
        
    with open(filename, 'w') as outfile:
        json.dump(file_data, outfile, indent=4)
    
add_label()