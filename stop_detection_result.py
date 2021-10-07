from stop_detection import stop_points
from shapely.geometry import Point
import geopandas

stop_points.to_file("data/result.json", driver="GeoJSON")

# str = '{['
#
# for i in range(len(stop_points.geometry)):
#
#     str2 = '{'
#     str2 = str2 + '"stop_id": '
#     str2 = str2 + stop_points.geometry.keys()[i]
#     str2 = str2 + ',"geometry": '
#     #str2 = str2 + stop_points.geometry[i]
#     #print(stop_points.geometry[i])
#     str2 = str2 + ',"start_time": '
#     str2 = str2 + stop_points.start_time[i]
#     str2 = str2 + ',"end_time": '
#     str2 = str2 + stop_points.end_time[i]
#     str2 = str2 + ',"traj_id": '
#     str2 = str2 + stop_points.traj_id[i]
#     str2 = str2 + ',"duration_s": '
#     str2 = str2 + stop_points.duration_s[i]
#     str2 = str2 + '}'
#     #print(str2)
#     if i<len(stop_points.geometry)-1:
#         str2 = str2 + ','
#     str = str + str2
#
# str = str + ']}'
#
#
#
#
#
#
#
# #print(stop_points.geometry[1])
#
#
# #print(stop_points.duration_s)
# #print(stop_points.start_time)
# #print(stop_points.end_time)
