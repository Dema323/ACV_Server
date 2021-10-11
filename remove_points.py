import json

def remove_points(filename='data/result.json'):
    correct_data = []

    with open(filename, 'r+') as file:
        file_data = json.load(file)

        for features in file_data['features']:
            if (features['properties']['duration_s'] < 60):
                if (features['properties']['backtracking'] == True):
                    correct_data.append(features)
            else:
                correct_data.append(features)

    with open('data/removed.json', 'a') as outfile:
        json.dump(correct_data, outfile, indent=4,separators=(',', ': '))



remove_points()
