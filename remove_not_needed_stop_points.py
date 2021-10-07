import json
from geopy import distance
import pandas as pd
from datetime import datetime
from datetime import date


def remove_not_needed_stop_points(filename='data/result.json'):
    start_time = 0
    end_time = 0

    end_times_resto = []
    start_times_client = []

    with open(filename, 'r+') as file:
        file_data = json.load(file)
        length = len(file_data['features'])
        for i in range(1, length - 1):
            #OPHAAL
            if (i % 2) == 1:
                end_time = pd.to_datetime(file_data['features'][i]['properties']['end_time'])
                print(end_time)
                end_times_resto.append(end_time)

            if (i % 2) == 0:
                start_time = pd.to_datetime(file_data['features'][i]['properties']['start_time'])
                print(start_time)
                start_times_client.append(start_time)

    # diff = start_times_client[0] - end_times_resto[0]
    # print(diff.total_seconds())

    for

        # print(length)
        # print(file_data['features'][1]['geometry']['coordinates'])

remove_not_needed_stop_points()


# import json
#
# json_data = json.dumps({
#   "result":[
#     {
#       "run":[
#         {
#           "action":"stop"
#         },
#         {
#           "action":"start"
#         },
#         {
#           "action":"start"
#         }
#       ],
#       "find": "true"
#     }
#   ]
# })
#
# item_dict = json.loads(json_data)
# print len(item_dict['result'][0]['run'])
