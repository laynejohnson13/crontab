##Import packages
import crontab
import os
import requests


COVID19 = requests.get('https://covid-19.dataflowkit.com/v1/USA')

print(COVID19.text)

COVID19.to_csv(‘/Users/laynejohnson/Desktop/crontab/data_10_2_22.csv)