import requests
import config

def get_puuid(region, api_key, summoner_name):
    api_url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + api_key
    repsonse = requests.get(api_url)
    player_info = repsonse.json()
    player_puuid = player_info["puuid"]
    return str(player_puuid)


def get_matches(puuid, api_key):
    api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?start=0&count=20" +"&api_key=" + api_key
    repsonse = requests.get(api_url)
    match_ids = repsonse.json()
    return str(match_ids)


puuid = get_puuid("na1", config.api_key, "M4NU")

matches = get_matches(puuid, config.api_key)
print(matches)
