# import streamlit as st
import numpy as np
import pandas as pd

import requests


API_KEY = "9qpfOevmLWlZvEGAJsul-C0Cyddrh9Oz4TPc6qPxuY0t"


token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

daily_time=68.95
age=35
areaincome=61833.9
dailyinternetuse=256.09
adtopicline='Cloned 5thgeneration orchestration'
city='Wrightburgh'
gender=0
country='Tunisia'
timestamp='2016-03-27 00:53:11'


input_features = [[daily_time, age, areaincome, dailyinternetuse, adtopicline, city, gender, country, timestamp]]

payload_scoring = {"input_data": [{"fields": [['daily_time','age','areaincome','dailyinternetuse','adtopicline','city','gender','country','timestamp']], "values": input_features}]}

response_scoring = requests.post('https://private.eu-de.ml.cloud.ibm.com/ml/v4/deployments/7eda709e-df60-46d0-87c9-9bac54561274/predictions?version=2021-05-01', json=payload_scoring,headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())

ans = response_scoring.json()['predictions'][0]['values']
print(ans)
finalprob = ans[0][1][0]

if finalprob > 50:
    print("Based on the above factors,the user Viewed the Advertisement")

else:
     print( "Based on the above factors,the user did not View the Advertisement")