import requests
import config

def get_puuid(region, api_key, summoner_name):
    api_url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + api_key
    response = requests.get(api_url)
    player_info = response.json()
    player_puuid = player_info["puuid"]
    return str(player_puuid)


def get_matches(puuid, api_key):
    api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?start=0&count=20" +"&api_key=" + api_key
    response = requests.get(api_url)
    match_ids = response.json()
    return str(match_ids)

def get_match_kills(match_id, puuid, api_key):
    api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/" + match_id + "?api_key=" + api_key
    response = requests.get(api_url)
    match_info = response.json()
    index_of_player = match_info["metadata"]["participants"].index(puuid)
    return index_of_player

puuid = get_puuid("na1", config.api_key, "M4NU")
print(puuid)

matches = get_matches(puuid, config.api_key)

kills = get_match_kills('NA1_4814488897', puuid, config.api_key)
print(kills)

