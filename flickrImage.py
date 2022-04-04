##IMPORT REQUIRED LIBRARIES
import json
import requests

#Get key for accessing Flickr
with open("secretKey.json", "r") as file:
  subscriptionKey = json.load(file)["flickrKey"]

#Create the web address we will be querying
webEndpoint = "https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={0}&tags={1}&per_page=1&format=json&nojsoncallback=1"

#Function to format the web address
def photoURL(tag:str):
  response = requests.get(webEndpoint.format(subscriptionKey,tag))
  imageData = response.json()["photos"]["photo"][0]
  photoLink = f"https://live.staticflickr.com/{imageData['server']}/{imageData['id']}_{imageData['secret']}.jpg"

#Function to process a statement and get a topic tag
def topicTag(sentence):
    topic = ''
    return photoURL(topic)