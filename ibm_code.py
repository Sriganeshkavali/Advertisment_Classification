import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://eu-de.dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html)
API_KEY = "9qpfOevmLWlZvEGAJsul-C0Cyddrh9Oz4TPc6qPxuY0t"


token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}

response_scoring = requests.post('https://private.eu-de.ml.cloud.ibm.com/ml/v4/deployments/7eda709e-df60-46d0-87c9-9bac54561274/predictions?version=2021-05-01', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())