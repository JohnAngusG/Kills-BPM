import requests
import config

def get_puuid(region, api_key, summoner_name):
    api_url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + api_key
    repsonse = requests.get(api_url)
    player_info = repsonse.json()
    player_puuid = player_info["puuid"]
    return print(player_puuid)

def get_matches(puuid, api_key):
    api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "&api_key=" + api_key
    repsonse = requests.get(api_url)
    match_ids = repsonse.json()
    return print(match_ids)


