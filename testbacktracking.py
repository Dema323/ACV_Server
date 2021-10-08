import json
import sys
import backtracking
import pandas as pd
from datetime import datetime
from datetime import date

def testbacktracking(filename='data/result.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)


        for features in file_data['features']:


            #backtrackingcompare(startx,endx)
            x = backtracking.backtrackingcompare(features)
            print(x)

testbacktracking()
