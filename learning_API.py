import requests
import config

## get player info 
request_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Perdón"
api_key = config.api_key
request_api = request_url + '?api_key=' + api_key
response = requests.get(request_api)

player_info = response.json()

print(player_info['puuid'])


## get match info

request_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/d5pNAtwAkhPf-cN2CMsAEjGFyRC9-xh0rD0qlfuKUNt3A2jW7asC2h-lL7akLwF0vsX_rF_ftLZlzg/ids?start=0&count=20"
request_api = request_url + '&api_key=' + api_key
response = requests.get(request_api)

matches_info = response.json()
print(matches_info[0]) ## 0 being most recent -1 or 19 being oldest

## get specific match information

request_url =  'https://americas.api.riotgames.com/lol/match/v5/matches/NA1_4813360622'
request_api = request_url + '?api_key=' + api_key
response = requests.get(request_api)

match_info = response.json()

participants = match_info['metadata']['participants']
print(participants.index(player_info['puuid']))

print(match_info['info']['participants'][7]['kills'])

## get for loop to add up all my kills

counter = 0
for match in matches_info:
    request_url =  'https://americas.api.riotgames.com/lol/match/v5/matches/' + match
    request_api = request_url + '?api_key=' + api_key
    response = requests.get(request_api)
    match_info = response.json()
    index_of_me = match_info['metadata']['participants'].index(player_info['puuid'])
    kills = match_info['info']['participants'][index_of_me]['kills']
    counter += kills


print(counter)

## get average of kills
print(counter / len(match_info))




