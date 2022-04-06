##IMPORT REQUIRED LIBRARIES
import json
import uuid
import requests

#Add your subscription key and endpoint
with open("secretKey.json", "r") as file:
  subscription_key = json.load(file)["bingKey"]
endpoint = "https://api.cognitive.microsofttranslator.com"

#Add your location, also known as region. The default is global. This is required if using a Cognitive Services resource.
location = "westus2"

#Get the webpath and concatenate it into the endpoint
path = '/translate'
constructed_url = endpoint + path

#Dictionary to save the API version, the language we are using, and the languages we are translating to
params = {
    'api-version':'3.0',
    'from':'en',
    'to':['fr-CA','zh-Hans','pa']
}

#Create the headers
headers = {
    'Ocp-Apim-Subscription-Key':subscription_key,
    'Ocp-Apim-Subscription-Region':location,
    'Content-type':'application/json',
    'X-ClientTraceId':str(uuid.uuid4())
}

#Create the function to be imported, which gets us our translations
def translate(body:list[dict]):
    request = requests.post(constructed_url,params=params,headers=headers,json=body)
    if request.status_code != 200:
        raise ValueError("Error : {}".format(request.json()['error']['message']))
    return [item['text'] for item in request.json()[0]['translations']]

#[{'text':"Hi, how are you?"}]