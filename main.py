'''
Prbolem Statment:


'''
import requests
import json
import pandas as pd

response = []
count = 0
maxVal = ''
#url = 'https://www.wsj.com/articles/crypto-hedge-fund-three-arrows-defaulted-on-loan-says-broker-voyager-digital-11656336534?page=1'
#r = requests.get(url,headers={"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})
#jsonData = json.loads(r.text)

while count != 1000:
    url = 'https://api.stocktwits.com/api/2/streams/symbol/ETH.X.json?filter=top&limit=20&max=+'+str(maxVal)
    r = requests.get(url)
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


