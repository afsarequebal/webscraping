'''
Prbolem Statment:

Scrape the text from the last 1000 tweets with the hashtag $ETH.X (Ethereum) posted on Stocktwits:

'''
import requests
import json
import pandas as pd

response = []
count = 0
maxVal = ''

while count != 1000:
    #Create URL to retrieve JSON/XML
    url = 'https://api.stocktwits.com/api/2/streams/symbol/ETH.X.json?filter=top&limit=20&max=+'+str(maxVal)

    #DO an API call
    r = requests.get(url)

    #parse the response
    jsonData = json.loads(r.text)
    msgArray = jsonData['messages']
    maxVal = jsonData['cursor']['max']
    for message in msgArray:
        count = count + 1
        user = message['user']
        data = {}
        data['id'] = user['id']
        data['username'] = user['username']
        data['timestamp'] = message['created_at']
        data['text'] = message['body']
        sentiment = message['entities']
        if message['entities']['sentiment']:
            data['tag'] = message['entities']['sentiment']['basic']
        response.append(data)

# saving the dataframe
df = pd.DataFrame(response)
df.to_csv('GFG.csv')


