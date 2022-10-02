##Import packages
import crontab
import os
import requests
import sys
import time
import pandas as pd

##importing API 
df = pd.read_json('https://data.covid19india.org/v4/min/data.min.json')

##saving as csv file
df.to_csv('csv/COVID19.csv', index = None)

##timestamp
currentTime = time.time()
listTime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(currentTime))
print('The current time is: ', listTime)

##getting cwd
cwd = os.getcwd()
print(cwd)

with open(cwd + '/updateFile_' + listTime + '.txt', 'w') as f:
    f.write(str(df))
