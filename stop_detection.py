
import pandas as pd
import geopandas as gpd
from datetime import datetime, timedelta
import numpy

import sys
sys.path.append("..")
import movingpandas as mpd
#print(mpd.__version__)

import warnings
warnings.simplefilter("ignore")

FSIZE = 350

df = gpd.read_file('data/output.geojson')
df['t'] = pd.to_datetime(df['t'])
df = df.set_index('t').tz_localize(None)
#print("Finished reading {} rows".format(len(df)))

traj_collection = mpd.TrajectoryCollection(df, 'trajectory_id')
traj_collection


my_traj = traj_collection.trajectories[0]
my_traj

detector = mpd.TrajectoryStopDetector(my_traj)


traj_plot = my_traj.hvplot(title='Trajectory {}'.format(my_traj.id), line_width=7.0, tiles='CartoLight', color='slategray', frame_width=FSIZE, frame_height=FSIZE)
traj_plot


#stop_durations = detector.get_stop_time_ranges(min_duration=timedelta(seconds=60), max_diameter=100)
stop_points = detector.get_stop_points(min_duration=timedelta(seconds=60), max_diameter=100)
# stop_segments =  detector.get_stop_segments(min_duration=timedelta(seconds=60), max_diameter=100)


# for x in stop_durations:
#     #print(x)

#print(stop_points)
